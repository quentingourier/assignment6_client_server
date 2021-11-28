#Test the model with test images
#here are some images located at: https://oreil.ly/dEUpx
#you can try your own images. note: the model is training on images with whitebackground


# os.add_dll_directory("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/NVIDIA Corporation/CUDA Samples/v11.5/bin")

import numpy as np
from tensorflow.keras.preprocessing import image
from keras.models import load_model


model = load_model('rps.h5')
 
def prediction(filename):
  # predicting images
  path = filename+'.png'
  img = image.load_img(path, target_size=(150, 150))
  x = image.img_to_array(img)
  x = np.expand_dims(x, axis=0)

  images = np.vstack([x])
  classes = model.predict(images, batch_size=10)
  # print(path)
  # print(classes)

  return classes

  #note: neurons are in alphabetical order by label