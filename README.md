# DreamWoodz
STEP 1
Create a virtual environment using the command "virtualenv venv"

STEP 2
Activate the virtual environment using the command "source venv/Scripts/activate"

STEP 3
Use  "pip install -r requirements.txt" to install the requirements.txt file 

To install the face recognition library in python, you will first need too have visual studio for C++ installed on your machine. 

If you don't already have visual studio installed on your machine you can visit the link below and follow the instructions to install dlib which is necessary for installing python's facial recognition library on windows.


https://www.geeksforgeeks.org/how-to-install-dlib-library-for-python-in-windows-10/

STEP 4
after all installations have been made run this command 

python manage.py makemigrations
python manage.py migrate 
python manage.py runserver

STEP 5

Copy and paste the localhost url into a webbrowser. The url will look like this "http://127.0.0.1:8000/"
