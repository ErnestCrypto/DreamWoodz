from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'


class AccountView(TemplateView):
    template_name = 'account.html'
    

class BedView(TemplateView):
    template_name = 'bed.html'


class ChairView(TemplateView):
    template_name = 'chair.html'


class ContactsView(TemplateView):
    template_name = 'contacts.html'


class DeskView(TemplateView):
    template_name = 'desk.html'


class FaceView(TemplateView):
    template_name = 'face.html'


class SofaView(TemplateView):
    template_name = 'sofa.html'


class WordropeView(TemplateView):
    template_name = 'wordrope.html'




