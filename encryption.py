from __future__ import division         # change the / operator to mean true division throughout the module.  always floating point result
from PIL import Image
from random import randint
from collections import deque
import smtplib


def rubics_operation(image, k):
    j = 0
    while j < len(image):
        sum_pix = sum(image[j])
        x = deque(image[j])                     #adding and removing elements from either end
        if sum_pix % 2 == 0:
            x.rotate(k)
        else:
            x.rotate(-k)

        image[j] = list(x)
        j +=1

    return image


def row_col_inversion(image):
    other = list()
    temp = list()
    i = 0
    while i < len(image[0]):
        temp = []
        for row in image:
            temp.append(row[i])
        other.append(temp)
        i += 1

    return other


def xor_operation(image, k):
    i = 1
    for row in image:
        if i % 2 == 0:
            j = 0
            temp_k = 255 - k
            for pix in row:
                row[j] = temp_k ^ pix
                j += 1
        else:
            j = 0
            for pix in row:
                row[j] = k ^ pix
                j += 1
    i += 1

    return image
    
def send_email(email, kr, kc, itr):
    email_adderss = 'imgencryption@gmail.com'
    email_password = 'minor123'

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(email_adderss, email_password)

        subject = "Image Encryption"
        body = 'Image encrypted successfully! kr = ', kr, ' kc = ', kc, 'Number of Iterations = ', itr

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(email_adderss, email, msg)    


def inputImg(file_name, itr, email):
    #file_name = input("enter the file name to be encrypt:\t")
    im = Image.open(file_name)          #image details
    pixels = list(im.getdata())
    grey_image1 = list()
    for pix in pixels:
        grey_image1.append(int(pix[0]))
    grey_image2 = list()
    sp = 0
    for rows in range(im.size[1]):
        fp = sp + im.size[0]            #length or size of list
        x = grey_image1[sp:fp]
        sp = fp
        grey_image2.append(x)

    #itr = int(input("enter the no of iterations :\t"))
    kr = randint(1, 255)

    kc = randint(1, 255)

    print("random integers are " + str(kr) + " , " + str(kc))

    #email = input("Enter email: ")
    send_email(email, kr, kc, itr)


    i = 0

    while i < itr:
        i += 1

        grey_image2 = rubics_operation(grey_image2, kr)

        grey_image2 = row_col_inversion(grey_image2)

        grey_image2 = rubics_operation(grey_image2, kc)

        grey_image2 = row_col_inversion(grey_image2)

        grey_image2 = xor_operation(grey_image2 , kr)

        grey_image2 = row_col_inversion(grey_image2)

        grey_image2 = xor_operation(grey_image2 , kc)




    grey_image3 = list()
    for row in grey_image2:
        for pix in row:
            grey_image3.append(pix)

    grey_image4 = list()

    for pix in grey_image3:
        x = (pix, pix, pix)
        grey_image4.append(x)
    # generating the output

    x, y = im.size
    im2 = Image.new("RGB", (x, y))

    im2.putdata(grey_image4)
    im2.save("enc_result/" + file_name)

    print("encryption done")
