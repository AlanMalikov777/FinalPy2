from django.shortcuts import render
from PIL import Image
# Create your views here.
from .form import ImageForm
import numpy as np
from .models import Images, Predict
from . import readpredict

dick = {'1':'airplane', '2':'automobile', '3':'bird', '4':'deer', '5':'dog', '6':'frog', '7':'horse', '8':'ship', '9':'truck'}


def index(request):
    if request.method == "POST":
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.instance
            elo = request.FILES
            bob = elo['image']
            print(bob)
            img = Image.open(bob)
            preds = readpredict.model_predict(img)
            print(preds[0])
            pred_class = np.argmax(preds[0])
            if (pred_class==0):
                pred_class=1
            result = dick[str(pred_class)]
            #pred_class = decode_predictions(preds, top=1)  
            print(result)
            form.save()
            p = Predict(predict = result)
            p.save()
            return render(request, "index.html", {"obj": obj, "res":result})
    else:
            form = ImageForm()
            img = Images.objects.all()
            pre = Predict.objects.all()
    return render(request, "index.html", {"img": img, "form": form, "pre":pre})
    # return render(request, "index.html")
