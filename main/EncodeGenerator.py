import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials, db, storage

#Database Crendentials, Database Service uses is Firebase and the database for the project is named "masmos"
cred = credentials.Certificate("/home/mashal/PycharmProjects/pythonProject/.venv/serviceAccounts.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "add-your-own-database-url",
    "storageBucket": "your-own-storage-bucket"

})


# Importing the Student images to a list
folderPath = '/home/mashal/PycharmProjects/pythonProject/Images'
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
studentIds = []
# print(modePathList)



# Gettiing the student ids from the images
for path in pathList:
    os.path.splitext(path)

    # Splitting the paths from the id
    studentId, _ = os.path.splitext(path)
    studentIds.append(studentId)
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
    # print(path)

    # # Sending images to the database
    # fileName = f'{folderPath}/{path}'
    # bucket = storage.bucket()
    # blob = bucket.blob(fileName)
    # blob.upload_from_file(fileName)


print(studentIds)
# print(len(imgList))


def findEncodings(imagesList):

    # Changing from bgr to rgb
    encodeList =[]
    for img in imagesList:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


print("Encoding Started ... ")
encodeListKnown = findEncodings(imgList)
print(encodeListKnown)
encodeListKnownWithIds = [encodeListKnown,studentIds]
print("Encoding Complete")


# Generating pickle file

file = open("EncodeFile.p",'wb')
pickle.dump(encodeListKnownWithIds,file)
file.close()
print("File Closed...")






