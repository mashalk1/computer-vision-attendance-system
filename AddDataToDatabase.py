import firebase_admin
from firebase_admin import credentials, db
#Database Crendentials, Database Service uses is Firebase and the database for the project is named "masmos"
cred = credentials.Certificate("/home/mashal/PycharmProjects/pythonProject/.venv/serviceAccounts.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "your-own-database-credentials"
})

# Directory for ids of the students in the database
ref = db.reference('Students')

# Update any values from here
data = {
    "1234": {
        "name": "Iron Man",
        "sId": "1234",
        "Dept": "CS",
        "total_attendance": "12",
        "lastAttendanceTime": "2023-11-2 1:11:12"
    },
    "1235": {
        "name": "Person2",
        "sId": "1235",
        "total_attendance": "14",
        "lastAttendanceTime": "2023-11-2 1:12:12"
    },
    "1236": {
        "name": "Person3",
        "sId": "1236",
        "total_attendance": "15",
        "lastAttendanceTime": "2023-11-2 1:13:12"
    },
    "1237": {
        "name": "Imran Khan",
        "sId": "1237",
        "total_attendance": "17",
        "lastAttendanceTime": "2023-11-2 1:18:12"
    },
    "21909": {
        "name": "Tariq Jameel",
        "sId": "21909",
        "total_attendance": "100",
        "lastAttendanceTime": "2023-11-2 1:18:12"
    },
    "218045":
        {
            "name": "Nomi",
            "sId": "218045",
            "total_attendance": "0",
            "lastAttendanceTime": "1980-12-10 1:10:10"
        },

}

# Iterate through the data and update the database
for key, value in data.items():
    ref.child(key).set(value)
