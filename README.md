# create-rgba-image
We can only store the RGBA image in png format.
The alpha channel is periodic from 1 to 256, if the value is out of this range, 
it still works, with the equal effect as the corresponding value in 1~256.
When the range is limited from 1 to 256, smaller the alpha value is, more transparent the image is. The larger the alpha is, less transparent the image is.
The RGBA images in png format are 32-bit images.
