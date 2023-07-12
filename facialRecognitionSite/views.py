from os import path
from urllib.request import urlopen
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from profiles.models import *
from .models import *
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile
from .forms import *
from django.contrib import messages
import face_recognition
import cv2
import numpy as np


def face(request):
    video_capture = cv2.VideoCapture(0)
    users = User.objects.all()
    known_face_encodings=[]
    known_face_names=[]
    sample_image_containers = []
    sample_face_encoding_containers = []
    context ={}
    pk=0
   
    for user in users:
    # Load a sample picture and learn how to recognize it.
        sample_image = face_recognition.load_image_file(f".{user.image.url}")
        sample_image_containers.append(sample_image)
        sample_face_encoding = face_recognition.face_encodings(sample_image)[0]
        sample_face_encoding_containers.append(sample_face_encoding)
        known_face_encodings.append(sample_face_encoding)
        known_face_names.append(str(user.id))
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Only process every other frame of video to save time
        if process_this_frame:
            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            # rgb_small_frame = small_frame[:, :, ::-1]
            rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(
                rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(
                    known_face_encodings, face_encoding)
                name = "Unknown"

                # # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(
                    known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame

        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35),
                        (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6),
                        font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Video', frame)
        
        if face_names:
            logged_user = User.objects.filter(id=face_names[0])
            pk = logged_user[0].id
            print(pk)
            break
        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()

    return redirect('facialRocognitionUrls:indexPage',pk)



def login_view(request):
    return render(request, 'login.html', {})


def logout_view(request):
    logout(request)
    redirect('login')


def find_user_view(request):
    # if able to find user
    return JsonResponse({'sucsess': True})


# @login_required
def home_view(request,pk):
    logged = User.objects.get(id = pk) 
    return render(request, 'index.html', {'pk':pk,'logged':logged})


class AboutView(TemplateView):
    template_name = 'about.html'
    def get(self,request,pk):
        logged = User.objects.get(id = pk) 
        return render(request, 'about.html', {'pk':pk,'logged':logged})



class AccountView(TemplateView):
    template_name = 'account.html'

    def post(self, request, format=None):
        user = UserForm(request.POST, request.FILES)
        # messages.success(request, f"{request.POST},{request.FILES}")
        if user.is_valid():
            user.save()
            return render(request, 'login.html', {})
        else:
            return render(request, 'account.html', {})


class BedView(TemplateView):
    template_name = 'bed.html'


class ChairView(TemplateView):
    template_name = 'chair.html'


class ContactsView(TemplateView):
    template_name = 'contacts.html'

    def get(self, request, pk):
        logged = User.objects.get(id=pk)
        return render(request, 'contacts.html', {'pk': pk, 'logged': logged})




class DeskView(TemplateView):
    template_name = 'desk.html'


class FaceView(TemplateView):
    template_name = 'face.html'


class SofaView(TemplateView):
    template_name = 'sofa.html'


class WordropeView(TemplateView):
    template_name = 'wordrope.html'
