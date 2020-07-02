from PIL import Image
import numpy  as np
import matplotlib.pyplot as plt

im = Image.open(".../cameraman.tif")
img=np.array(im)

new=[]
count=0
#find histogram
for i in range(256):
    for j in range(img.shape[1]):

        for k in range(img.shape[0]):

            if img[j][k]==i-1:
                count+=1
    new.append(count)
    count=0
print(new)

summ=0
for i in range(len(new)):
    summ+=(i*new[i])

median1=summ/65536

#calculate mean 
def mean(a,th1,th2):
    summ=0
    count=0
    for i in range(th1,th2):
        summ+=(i*new[i])
        count+=new[i]
    m=summ/count
    return m

previousThreshold=new[1]
nextThreshold=median1

#loop until previous threshold is equals to next threshold
while(previousThreshold!=nextThreshold):
    previousThreshold=nextThreshold
    m1=mean(new,1,round(previousThreshold))
    m2=mean(new,round(previousThreshold+1),len(new))
    nextThreshold=(m1+m2)/2
    nextThreshold=round(nextThreshold)

print(nextThreshold)

#assign gray value(255) to image values greater than 90(next threshold)
for i in range(256):
    for j in range(256):

        if img[i][j]>nextThreshold:
            img[i][j]=255
        else:
            img[i][j]=0


print(img)
image2 = Image.fromarray(img)
image2.show()
