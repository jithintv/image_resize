from django.urls import path
from . import views

urlpatterns = [

        path('', views.index, name='index.html'),
        path('index.html', views.index, name='index.html'),
        path('upload.html',views.hotel_image_upload, name= 'upload')
]
