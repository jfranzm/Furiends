from django.shortcuts import render, redirect
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
