# create-rgba-image
We can only store the RGBA image in png format.
The alpha channel is periodic from 0 to 255, if the value is out of this range, 
it still works, with the equal effect as the corresponding value in 0~255.
When the range is limited from 0 to 255, smaller the alpha value is, more transparent the image is. The larger the alpha is, less transparent the image is.
The RGBA images in png format are 32-bit images.
