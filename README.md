# Thresholding

__Image segmentation can be done using Thresholding.__

__Isodata and otsu are image segmentaton techniques using thresholding.__ 

__Isodata thresholding:__

1)Find the histogram of the image.

2)Calculate the mean.

3)Loop until previous threshold is not equal to next threshold.

__while(previousThreshold!=nextThreshold):__
    
    previousThreshold=nextThreshold
    
    m1=mean(new,1,round(previousThreshold))
    
    m2=mean(new,round(previousThreshold+1),len(new))
    
    nextThreshold=(m1+m2)/2
 
    nextThreshold=round(nextThreshold)

4)Convert image into binary image by assigning, pixel values above threshold as 255 and and pixel values below threshold as 0.
