import numpy as np
import matplotlib.pyplot as plt
import cv2
import glob
from matplotlib import image

#Reading Dataset
image_list = []
for filename in glob.glob('yalefaces/yalefaces/*'):
    im = image.imread(filename)
    image_list.append(im)
    
x, y = image_list[0].shape

#Flattening
f_img = []
for img in image_list:
    t = img.flatten()
    f_img.append(t)
f_img = np.matrix(f_img)

pc = 145
#Calculating Eigen Vectors and Mean
mean, eigenVectors = cv2.PCACompute(f_img, mean=None, maxComponents = pc)

#Calculating Weight
et = np.transpose(eigenVectors)    
d = f_img.shape
weights = (f_img - mean).dot(et)

#Reconstruction
rec_faces = weights.dot(eigenVectors)
f_s = rec_faces[0] + mean

#Plotting
plt.imshow(f_s.reshape(x,y), cmap = 'gray')
plt.title('Number of Principal Components:' + str(pc)) 
plt.show()
print('Number of Principal Components:', pc)
plt.imshow(image_list[0], cmap = 'gray')
plt.title("Original Image")
plt.show()