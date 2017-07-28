from PIL import Image

darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

my_image = Image.open("mercury.jpg")#mercury, wave, afghan, and nature look really cool
image_list = my_image.getdata()
image_list = list(image_list)

recolored = []

for x in image_list:
    intensity = x[0] + x[1] + x[2]
    if intensity <= 182:
        recolored.append(darkBlue)
    elif 182 < intensity <= 364:
        recolored.append(red)
    elif 364 < intensity <= 546:
        recolored.append(lightBlue)
    elif (intensity)>546:
        recolored.append(yellow)




new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("recolored.jpg", "jpeg") #save the new image as "recolored.jpg"
