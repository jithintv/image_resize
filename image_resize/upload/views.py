from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from PIL import Image
from django.core.files.storage import FileSystemStorage
import time
import glob
import os
from django.conf import settings


def index(request):
	obj=upload_new.objects.all()

	return render(request, 'index.html',{'obj':obj})


def hotel_image_upload(request):
	if request.method == 'POST':
		image = request.FILES['photo']
		name = request.POST.get('name')
		width1 = int(request.POST.get('width'))
		height1 = int(request.POST.get('Height'))
		print(width1)
		print(height1)
		im = Image.open(image)
		width, height = im.size
		print(width)
		print(height)
		newsize = (width1, height1)
		im = im.resize(newsize)
		filename = settings.MEDIA_ROOT + '\scr{}.jpg'
		filename1 = settings.MEDIA_ROOT + '\*'
		if im.mode in ("RGBA", "P"):
			im = im.convert("RGB")
		im.save(filename.format(int(time.time())))
		list_of_files = glob.glob(filename1)
		latest_file = max(list_of_files, key=os.path.getctime)
		latest_file = os.path.basename(latest_file)

		data = upload_old()
		data.old_name = name
		data.old_Image = image
		data.save()

		data1 = upload_new()
		data1.new_name = name
		data1.new_Image = latest_file
		data1.save()

	return render(request, 'upload.html')