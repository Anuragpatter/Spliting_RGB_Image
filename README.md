# Spliting_RGB_Image
A Python Project to split a three channeled (RGB) colorful image into three single channeled images representing Red Channel, Green Channel, Blue Channel.

# Description
In this project we use python library OpenCV to convert an RGB image to grayscale and print the image array (value of each pixels) of grayscale and RGB, print its shape and then split the image into 3 single channeled images.

# Requirements
Install OpenCV and NumPy libraries in your system to be used for the project.<br> 
OpenCV and NumPy can be directly downloaded and installed with the use of pip (package manager).<br>
To install OpenCV and NumPy, just go to the command-line and type the following command:

```
pip install opencv-python
```

```
pip install numpy
```

# Working
**1. We import cv2 (OpenCV) module to our work space.**
**2. Read the image by using 'imread' function and providing image path as an argument.**

![2016599](https://github.com/Anuragpatter/Spliting_RGB_Image/assets/93168851/449f32e1-0e0e-4e0c-b196-9c550b5abe8e)

**3. Converting the image to grayscale, then printing image array and shape.**

![gray_array](https://github.com/Anuragpatter/Spliting_RGB_Image/assets/93168851/169f0278-5511-4d89-a9aa-5dcce67ed571)

As you can see, the printed array is a two dimensional array, in which each number represents a pixel and the value of the number is the intensity of light in that pixel. As each number in the above image array represents a pixel, it is called a single channeled image. The light intensity of each pixel in computer vision is measured from 0 to 255 and is known as the pixel value. When the pixel value is 0 it is black and when the pixel value is 255 it is white. Since we used OpenCV to read the image array, the dimensions of the above array are of the form height x width. Here the image has 768 pixels along it’s y-axis(height) and 1280 pixels along its x-axis(width).

**4. Converting image to RGB. Again print the array and shape.**

![RGB1](https://github.com/Anuragpatter/Spliting_RGB_Image/assets/93168851/0310640f-141f-4398-a8c9-04e6c952313c)<br>
![RGB2](https://github.com/Anuragpatter/Spliting_RGB_Image/assets/93168851/7dc08750-a519-44a3-9d41-926e06f10bd6)

The output is a three dimensional array this time! In this image each pixel has three channels. Each array in the second dimension, represents a pixel. The 0th index has the intensity of red light, the 1st index the intensity of green light and the 2nd index, the intensity of blue light. When you print the shape of this image, it prints a tuple containing the height, width and the number of channels. When you multiply these three values you get the total number of values inside the image array.

**5. We split the image into three channels by using 'split' function of OpenCV and then display these three images.**

# OUTPUT
**RED CHANNELED IMAGE:**
![R](https://github.com/Anuragpatter/Spliting_RGB_Image/assets/93168851/1dca5b52-7f12-4079-94aa-29f38594cdd5)<br>


**GREEN CHANNELED IMAGE:**
![G](https://github.com/Anuragpatter/Spliting_RGB_Image/assets/93168851/7f91b33f-4665-401a-847c-78f5ca28d751)<br>


**BLUE CHANNELED IMAGE:**<br>
![B](https://github.com/Anuragpatter/Spliting_RGB_Image/assets/93168851/e13c624b-5065-40fa-bb13-5e609e3ead28)<br>

Now, to know the difference between these three single channeled images, compare each image with the original image. Let us take the red channel image. You can see that the regions containing red colour in the original image are lighter in the red channel image. This simply means that, regions which contribute more to the red colour of the original image are lighter in the grayscale image of the red channel. And the regions which contribute less or do not contribute are dark. This applies for all the three channels.
