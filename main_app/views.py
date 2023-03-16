from django.shortcuts import render, redirect
import uuid
import boto3
from .models import Photo,Post
from django.views.generic import ListView, DetailView, CreateView
# Add the two imports below
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from .forms import PictureForm
from datetime import date
from django.utils import timezone 
from django.views.decorators.csrf import csrf_exempt

BUCKET = 'furiends'
S3_BASE_URL = f'https://{BUCKET}.s3.ca-central-1.amazonaws.com'

@csrf_exempt
def index(request):
    photos = Photo.objects.all()
    # print(photos)
    return render(request, "registration/login.html", {'photos': photos})

@csrf_exempt
def login_auth(request):
    print(request.POST)
    username = request.POST['username']
    password = request.POST['password']
    user_id = User.objects.get(username=username)
    print(user_id.id)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        return render(request, 'home.html', {'user_id': user_id.id})
        # Redirect to a success page.
    else:
        return render(request, '/')

def add_photo(request, user_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = 'furiends/' + uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}/{key}"
            print(url)
            print(user_id)            
            user = User.objects.get(pk=user_id)
            print(user)
            # print(type(date.today()))
            Photo.objects.create(url=url, user=user, likes = 1, caption='bird', category=2)
            print('done')
        except:
            print('An error occurred uploading file to S3')
    return render (request, 'home.html', {'user_id': user_id})

# Create your views here.
def home(request):
    user_id = request.user.id
    print(user_id)
    picture_form = PictureForm()
    return render(request, 'home.html', {
        'picture_form': picture_form, 'user_id':user_id
    })


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

def about(request):
    return render(request, 'about.html')

def my_profile(request):
    return render(request, 'my_profile.html')

def post_detail(request, post_id):
  post = Post.objects.get(id=post_id)
  return render(request, 'my_profile/post_detail.html', {'post': post
  })

def add_picture(request, user):
    form = PictureForm(request.POST)
    if form.is_valid():
        new_picture = form.save(commit=False)
        new_picture.picture_id = user
        new_picture.save()
    return render('home.html')

def PostCreate(request):
  return render(request, 'post_form.html')
  
