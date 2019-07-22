from django.urls import path, include

import classifier.views

app_name = 'bookedApp'

urlpatterns = [
    path('UploadPhoto/', classifier.views.UploadPhoto, name = 'UploadPhoto'),
]   