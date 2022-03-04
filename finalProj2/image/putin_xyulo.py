import tensorflow as tf;
import numpy as np;
import os;
from tensorflow.keras.applications.imagenet_utils import preprocess_input
from tensorflow.keras.preprocessing import image

def model_predict(img):
    model = tf.keras.models.load_model(os.getcwd() +'\image\modelss')
    img = img.resize((32, 32))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x, mode='tf')
    preds = model.predict(x)
    return preds
