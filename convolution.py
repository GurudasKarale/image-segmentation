from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

image=Image.open('C:/Users/Mohit K/Desktop/datasets/cameraman.tif')

data=np.asarray(image)
print(data.shape)
kernel=np.asarray(([0,1,0],[1,-4,1],[0,1,0]))   #high pass filter kernel
#kernel2=np.asarray(([1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]))  low pass filter kernel
r=data.shape[0]
c=data.shape[1]

a = np.zeros([256, 256], dtype = int)

for k in range(1,r-1):
    for l in range(1,c-1):
        sum=0
        for i in range(3):

            for j in range(3):
                sum+=kernel[i][j]*data[k+i-1][l+j-1]

        a[k][l]=sum

print(a)
image2 = Image.fromarray(a)
image2.show()
