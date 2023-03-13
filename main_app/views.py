from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
# Add the two imports below
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
import uuid
import boto3
from .models import Photo

S3_BASE_URL = 'https://s3-accesspoint.ca-central-1.amazonaws.com'
BUCKET = 'furiends'

def add_photo(request, picture_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = 'furiends/' + uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            Photo.objects.create(url=url, picture_id=picture_id)
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', picture_id=picture_id)
# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
