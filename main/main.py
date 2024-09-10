import os
import pickle
import numpy as np
import cv2
import time
import cvzone
import face_recognition
import firebase_admin
from firebase_admin import credentials, db, storage

#Database Crendentials, Database Service uses is Firebase and the database for the project is named "masmos"
cred = credentials.Certificate("/home/mashal/PycharmProjects/pythonProject/.venv/serviceAccounts.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "add-your-own-firebase-url-here"
})


cap = cv2.VideoCapture(0)  # Use 0 for the default camera (you can change it to 1 if you have an additional camera)
cap.set(3, 640)
cap.set(4, 480)

imgBackground = cv2.imread('/home/mashal/PycharmProjects/pythonProject/Resources/bgImage.png')


# Importing the modes images to a list
folderModePath = '/home/mashal/PycharmProjects/pythonProject/Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
# print(modePathList)
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath,path)))
# print(len(imgModeList))



# Loading the encoding file
print("Loading Encode File...")
file  = open('EncodeFile.p','rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
print(studentIds)
print("Encode File Loaded!")


modeType = 0
counter = 0
id = -1





while True:
    success, img = cap.read()

    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)


    # Feeding the new Values from the input to
    # MasMos to find and match encodings
    # from the new one to the saved oness
    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS,faceCurFrame)


    # # Setting the display on top of the bgimage
    imgBackground[162:162+480,55:55+640] = img
    # # To index the mode, upon 0, its the first image and then goes on
    imgBackground[44:44+600, 868:868+330] = imgModeList[modeType]



    # Comparing the encodings
    for encodeFace, faceLoc in zip(encodeCurFrame,faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
        # print("matches",matches)
        # print("face Distance",faceDis)


        # Making use of the matching values, 0 for false , 1 for true
        matchIndex = np.argmin(faceDis)
        # print("Match Index", matchIndex)

        if matches[matchIndex]:
            print("Known Face Detected")
            print(studentIds[matchIndex])
            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            bbox = 55+x1,162+y1,x2-x1,y2-y1
            imgBackground = cvzone.cornerRect(imgBackground,bbox,rt=0)

            id = studentIds[matchIndex]

            if counter == 0:
                counter = 1

            if counter != 0:
                # Retrieving data from database
                if counter == 1:
                    print(f'Retrieving data for ID: {id}')
                    studentInfo = db.reference(f'Students/{id}').get()
                    print(studentInfo)
                counter += 1



    cv2.imshow("Webcam", img)
    cv2.imshow("Face Attendance", imgBackground)
    cv2.waitKey(1)



cap.release()
cv2.destroyAllWindows()
