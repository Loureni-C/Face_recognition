##############################Código 1 mostrar rostinhos

from PIL import Image
import face_recognition

##image = face_recognition.load_image_file("./dontknow/DSC_6974.JPG")
image = face_recognition.load_image_file("./dontknow/IMG_4747.JPG")


face_locations = face_recognition.face_locations(image)


for face_location in face_locations:
    top, right, bottom, left = face_location
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()
##    #pil_image.save("{}.jpg".format(top))
print(face_locations)
print(len(face_locations))


##############################Código 2 comparar rostos em fotos dierentes
##foto individual pelo amor de Deus

##import face_recognition
##
##picture_of_me = face_recognition.load_image_file("./know/loureni.jpg")
##my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
##
##
##unknown_picture = face_recognition.load_image_file("./dontknow/DSC_6975.JPG")
##unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
##
##results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)
##if results[0] == True:
##    print("It's a picture of me!")
##else:
##    print("It's not a picture of me!")




##############################Código 3 junção dos anteriores

##from PIL import Image
##import face_recognition
##
##
##picture_of_me = face_recognition.load_image_file("./know/loureni.jpg")
##my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
##
##
##face_locations = face_recognition.face_locations(picture_of_me)
##
##for face_location in face_locations:
##    top, right, bottom, left = face_location
##    face_image = picture_of_me[top:bottom, left:right]
##    pil_image = Image.fromarray(face_image)
##    pil_image.show()
##
##
##print("Foto 1: ",len(face_locations),"---", face_locations)
###unknown_picture = face_recognition.load_image_file("./dontknow/IMG_4851.JPG")
###unknown_picture = face_recognition.load_image_file("./dontknow/IMG_4850.JPG")
###unknown_picture = face_recognition.load_image_file("./dontknow/IMG_4846.JPG") ##2 rostos
##unknown_picture = face_recognition.load_image_file("./know/regina.jpg")
##
##unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
##
##face_locations2 = face_recognition.face_locations(unknown_picture)
##
##for face in face_locations2:
##    top, right, bottom, left = face
##    face_image2 = unknown_picture[top:bottom, left:right]
##    pil_image2 = Image.fromarray(face_image2)
##    pil_image2.show()
##
##print("Foto 2: ",len(face_locations2),"---", face_locations2)
##
##results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)
##if results[0] == True:
##    print("It's a picture of me!")
##else:
##    print("It's not a picture of me!")



##############################Código 4  mostrar codificação 128
##
##
##from PIL import Image
##import face_recognition
##
##image = face_recognition.load_image_file("./dontknow/IMG_4498.JPG") ##many faces
##face_locations = face_recognition.face_locations(image)
##list_of_face_encodings = face_recognition.face_encodings(image)
##
##print(list_of_face_encodings)
##print(list_of_face_encodings[0])
##
##
##for face_location in face_locations:
##    top, right, bottom, left = face_location
##    face_image = image[top:bottom, left:right]
##    pil_image = Image.fromarray(face_image)
##    pil_image.show()


##############################Código 5 comparar 2 rostos iguais e mostrar codificação

##import face_recognition
##
##picture_of_me = face_recognition.load_image_file("./know/loureni.jpg")
##my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
##
##
##unknown_picture = face_recognition.load_image_file("./dontknow/IMG_4858.JPG")
##unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
##
##results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)
##if results[0] == True:
##    print("It's a picture of me!")
##else:
##    print("It's not a picture of me!")
##
##print('primeira: ',my_face_encoding,'\n')
##print('sssssssssssssssssssssssssssssss ',len(results),'\n')
##print('segunda: ',unknown_face_encoding,'\n')
##print('ddddddddddddddddddddddd ',results,'\n')
##
##

