# FinalPy2 - Keras
The program takes an photo and Keras,API designed for human being, provide the name of the thing in the picture.
To train and evaluate Keras were used CIFAR images and 2 stacks: Conv2D and MaxPooling2D.

Conv2D is a layer used by Keras that divides an image to tensors.

MaxPooling2d is a layer used by Keras that decreases the input size window by using the 2d array created by attributes "pool_size".

For testing program used it 3 times, because it increases accuracy of the result that Keras should give.

Also program uses PIL - library for working with images.
# Installation
You need to download all things that were shown in the requirements
and you need to download the repository of a program from Github.

Django, Pillow, Tensorflow-cpu, numpy, django-heroku, whitenoise, gunicorn
# Usage
``` bash
python manage.py makemigrations
python manage.py migrate   
python manage.py runserver
```
After that you need to go by link that was given by program.
# Examples
You need to upload image and it will save:
![image](https://user-images.githubusercontent.com/77801087/156753306-c6a7d325-1e93-4827-a5ea-bfc7ef6bac14.png)
![image](https://user-images.githubusercontent.com/77801087/156753002-16dfb53d-098a-4379-9360-93284925cb34.png)
and file will be saved in Postgresql:
![image](https://user-images.githubusercontent.com/77801087/156753136-4f1ff675-0769-4467-b381-fd33ea312447.png)

so you can use link heroku:

https://finalpython2.herokuapp.com/

# License
[MIT](https://choosealicense.com/licenses/mit/)
