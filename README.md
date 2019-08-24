# LC-classifier

A barebones web application built on Django to test my first ever Deep Learning model.

## Image Classification

The "LC" stands for Leopard and Cheetah. This web app lets users upload images of a leopard or a cheetah
and then classifies the image into one of the two categories.

The model was trained on around 400 images of each category. The images were all downloaded from Google Images.
The model was created using the fastai and PyTorch libraries. All the Deep Learning magic lies inside the `export.pkl` file, which is managed using Git LFS as it is 85MB in size.

## Setup

Steps to setup the project in a Linux environment:

* Make sure you have Python 3 installed on your machine (You can follow [this](https://docs.python-guide.org/starting/install3/linux/) guide)

* Go to the directory where you want to store this project and clone it there:
  `git clone https://github.com/shivanshu1234/LC-classifier.git`
  
* Now, it is highly recommended that you create a virtual environment for this project, follow [this](https://docs.python-guide.org/dev/virtualenvs/#virtualenvironments-ref) guide if you're not familiar with virtuals envs.

* After creating and activating a virtual env, got to the directory with the `requirements.txt` file and run `pip3 install -r requirements.txt` to install the dependencies. This step will require some time and a decent internet connection to complete.

* Now go to the directory with the `manage.py` file and run `python manage.py migrate`. This will create the database for your app.

* Lastly, run `python manage.py runserver`. If everything worked accordingly, you should now be able to access the app through a browser at 127.0.0.1:8000/classifier/UploadPhoto/ 

