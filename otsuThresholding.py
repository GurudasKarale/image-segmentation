from PIL import Image
import numpy  as np
import matplotlib.pyplot as plt

im = Image.open(".../cameraman.tif")
img=np.array(im)

new=[]
count=0
for i in range(256):
    for j in range(img.shape[1]):

        for k in range(img.shape[0]):

            if img[j][k]==i-1:
                count+=1
    new.append(count)
    count=0
print(new)

n=sum(new)
p=[]
for i in range(len(new)):       #probability of every gray level
    p.append(new[i]/n)

print(p)


def mean(a,th1,th2):               #mean
    summ=0
    count=0
    for i in range(th1,th2):
        summ+=(i*a[i])
        count+=a[i]
    m=summ/count
    return m

def variance(u,a,th1,th2):        #variance
    summ=0
    count=0
    for i in range(th1,th2):
        summ+=(np.square(i-u)*a[i])
        count+=a[i]
    m=summ/count
    return m


va=[]
for i in range(9,254):

    wb=sum(p[8:i])
    wf=sum(p[i+1:255])

    u1=mean(new,8,i)
    u2=mean(new,i+1,255)
    var1=variance(u1,new,8,i)
    var2=variance(u2,new,i+1,255)
    varWithin=(wb*var1)+(wf*var2)
    va.append(varWithin)                  #within class variance

print(va)
x=va.index(min(va))                      #index of within class variance
print(x)

for i in range(256):
    for j in range(256):

        if img[i][j]>x+8:          #threshold including removed zeros
            img[i][j]=255
        else:
            img[i][j]=0


print(img)
image2 = Image.fromarray(img)
image2.show()
