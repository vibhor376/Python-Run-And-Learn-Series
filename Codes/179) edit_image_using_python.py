from PIL import Image,ImageEnhance,ImageFilter
import os

img1=Image.open('gameengineering1.jpg') # this will open the image
img1.show() # this will display the image 
img1.save('gameengineering1.png') # this will save the image
Max_size=(300,150)
img1.thumbnail(Max_size)  # this will resize the image
img1.save('gameengineering(300x150).jpg')

# Below is an example how to convert all the '.jpg' files into '.png'
for i in os.listdir(r'D:\ieeepromo(materials)\game engineering'):
    if i.endswith('.jpg'):
        img=Image.open(i)
        f_n,e_n=os.path.splitext(i) # this will split the name for example 'image.jpg' as 'image' '.jpg'
        img.save(f'{f_n}.png')

img2=Image.open('gameengineering2.jpg')
sharp=ImageEnhance.Sharpness(img2)
# Note: 0 --> blurry image, 1 --> original image, >1 --> sharpness increased 
sharp.enhance(5).save('gameengineering2(sharpness increased).jpg')
sharp.enhance(0).save('gameengineering2(sharpness decreased).jpg')

color=ImageEnhance.Color(img2)
# Note: 0 --> black and white image, 1 --> original image, >1 --> color increased 
color.enhance(0).save('gameengineering2(black and white).jpg')
color.enhance(2).save('gameengineering2(color increased).jpg')

bright=ImageEnhance.Brightness(img2)
# Note: 0 --> black image, 1 --> original image, >1 --> brightness increased
bright.enhance(0).save('gameengineering2(black).jpg')
bright.enhance(1.5).save('gameengineering2(brightness increased).jpg') 

cont=ImageEnhance.Contrast(img2)
# Note: 0 --> bad contrast, 1 --> original image, >1 --> contrast increased
cont.enhance(0).save('gameengineering2(bad contrast).jpg')
cont.enhance(2).save('gameengineering2(high contrast).jpg')

img1.filter(ImageFilter.GaussianBlur(radius=4)).save('gameengineering1(gaussian blur).jpg') # by default radius=2