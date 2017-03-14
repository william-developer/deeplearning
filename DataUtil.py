import os
import numpy as np
from PIL import Image
def load(path):
    imgs = os.listdir(path)
    data = np.empty((25000,299,299,3),dtype="float32")
    label = np.empty((25000,),dtype="uint8")
    num = len(imgs)
    for i in range(num):
        img = Image.open(os.path.join(path,imgs[i]))
	img = img.resize((299,299))
	arr = np.asarray(img,dtype="float32")
	data[i,:,:,:] = arr
	t=imgs[i].split('.')[0]
	if t=='dog' :
		label[i] =1
	else :
		label[i] =0	
    return data,label
if __name__ == "__main__":
	data,label=load('data')
	print data 
