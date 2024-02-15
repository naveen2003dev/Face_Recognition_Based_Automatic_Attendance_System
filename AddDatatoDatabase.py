import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-attendance-76889-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "0928CS201059":
        {
            "name": "Naveen",
            "Branch": "CSE",
            "starting_year": 2020,
            "total_attendance": 0,
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "0928CS201032":
        {
            "name": "Dushyant",
            "Branch": "CSE",
            "starting_year": 2020,
            "total_attendance": 0,
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "0928CS201039":
        {
            "name": "Himanshu",
            "Branch": "CSE",
            "starting_year": 2020,
            "total_attendance": 0,
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "0928CS201075":
        {
            "name": "Priyansh",
            "Branch": "CSE",
            "starting_year": 2020,
            "total_attendance": 0,
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
}

for key, value in data.items():
    ref.child(key).set(value)
