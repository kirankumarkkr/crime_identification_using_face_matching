from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import ComplaintForm, SignUpForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from .forms import CriminalForm
from .forms import PhotoUploadForm
from .models import Complaint, Criminal
import face_recognition
import numpy as np

def home(request):
    return render(request, 'home.html')

def user_login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        # form = LoginForm(request.POST)
        # if form.is_valid():
        #     email = form.cleaned_data.get('email')
        #     password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Invalid email or password')
    else:
        form = LoginForm()
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
    
        user=User.objects.create_user(username,email,password1)
        user.save()
        messages.success(request, f'Account created for {username}!')
        return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def user_logout(request):
    logout(request)
    
    return redirect('home')


@user_passes_test(lambda u: u.is_superuser)
def upload_criminal(request):
    if request.method == 'POST':
        form = CriminalForm(request.POST, request.FILES)
        if form.is_valid():
            photo = request.FILES['photo']

            image = face_recognition.load_image_file(photo)
            face_encodings = face_recognition.face_encodings(image)

            if face_encodings:
                face_encoding = face_encodings[0]
                form.save()
                messages.success(request, 'Criminal uploaded successfully.')
                return redirect('home')
            messages.error(request,'no face detected.')
            return redirect('upload_criminal')
        else:
            messages.error(request,'invalid data.')
            return redirect('upload_criminal')
    else:
        form = CriminalForm()
    return render(request, 'upload_criminal.html', {'form': form})


def complaints(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Complaint taken successfully.')
            return redirect('home')
        else:
            messages.error(request,'invalid data.')
            return redirect('complaints')
    else:
        form = ComplaintForm()
    return render(request, 'complaints.html', {'form': form})


def detect(request):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.cleaned_data['photo']
            # Process the photo
            image = face_recognition.load_image_file(photo)
            face_encodings = face_recognition.face_encodings(image)
            if face_encodings:
                face_encoding = face_encodings[0]
                criminals = Criminal.objects.all()
                matches = []
                for criminal in criminals:
                    if criminal.face_encoding:
                        criminal_encoding = np.frombuffer(criminal.face_encoding)
                        distance = face_recognition.face_distance([criminal_encoding], face_encoding)
                        if distance < 0.6:  
                            matches.append((criminal, distance))
                
                if matches:
                    matches.sort(key=lambda x: x[1])  # Sort by distance
                    criminal = matches[0][0]
                    id=criminal.id
                    print(id)
                    complaint = Complaint.objects.filter(criminal_id=criminal.id)
                    print(complaint)
                    return render(request, 'result.html', {'criminal': criminal ,'complaint' : complaint})
            messages.error(request, 'No match found.')
            return redirect('detect')
    else:
        form = PhotoUploadForm()
    return render(request, 'detect.html', {'form': form})

def search(request):
    if request.method=='POST':
        name = request.POST['searchname']
        criminal = Criminal.objects.filter(name__icontains=name)
        return render(request, 'searchresult.html',{'criminal': criminal})
    return render(request, 'search.html')

def criminal_list(request):
        list = Criminal.objects.all()
        print(list)
        return render(request,'criminal_list.html',{'list':list})

