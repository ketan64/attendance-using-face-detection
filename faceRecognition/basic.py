import cv2
import numpy as np
import face_recognition

#import image and convert to rgb
img = face_recognition.load_image_file('test pic/rdj.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('test pic/rdj test.jpg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

#find face locations, encode faces, and show rectangle on encoded faces
faceLoc = face_recognition.face_locations(img)[0]
encode_img = face_recognition.face_encodings(img)[0]
cv2.rectangle(img,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encode_imgTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)

results = face_recognition.compare_faces([encode_img],encode_imgTest)
faceDist = face_recognition.face_distance([encode_img],encode_imgTest)
print(results,faceDist)

cv2.putText(imgTest,f'{results} {round(faceDist[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

#show output
cv2.imshow('RDJ',img)
cv2.imshow('test',imgTest)
cv2.waitKey(0)



