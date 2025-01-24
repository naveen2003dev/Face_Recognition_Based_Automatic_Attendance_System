import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "Firebase Database URL"
})

ref = db.reference('Students')

data = {
    "0888CS205461059":
        {
            "name": "Naveen",
            "Branch": "CSE",
            "starting_year": 2020,
            "total_attendance": 0,
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "09885CS20105632":
        {
            "name": "Dushyant",
            "Branch": "CSE",
            "starting_year": 2020,
            "total_attendance": 0,
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "09285335CS20159":
        {
            "name": "Himanshu",
            "Branch": "CSE",
            "starting_year": 2020,
            "total_attendance": 0,
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "0928CS205656575":
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
