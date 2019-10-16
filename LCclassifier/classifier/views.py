from fastai.vision import load_learner, open_image
from django.shortcuts import render, redirect
# import PIL.Image

from .models import Image
from .forms import PictureForm

def UploadPhoto(request):

    image_object = Image()
    context={}
    uploaded = False
    learn = load_learner('classifier')

    if request.method == "POST":
        
        form = PictureForm(request.POST, request.FILES, instance = image_object)
        if form.is_valid():
            image_object = form.save(commit = False)
            image_object.save()
            uploaded = True
            
            context['image_url'] = image_object.image.url
            image = request.FILES['image']
            # image = PIL.Image.open(image)
            
            image = open_image(image)
            prediction = learn.predict(image)
            print(prediction)
            context['prediction'] = prediction[0]

    form = PictureForm(instance = image_object)
    
    context['form']=form
    context['uploaded']=uploaded

    return render(request, template_name = 'classifier/photo_upload.html', context=context)
