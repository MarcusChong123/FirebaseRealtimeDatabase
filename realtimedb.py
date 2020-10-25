import pyrebase

config = {
    "apiKey": "yourapikey",
    "authDomain": "yourauthdomain",
    "databaseURL": "yourdatabaseURL",
    "projectId": "yourprojectid",
    "storageBucket": "yourstoragebucket",
    "messagingSenderId": "yourmessagingsenderid",
    "appId": "yourappID"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

# Create data

# time-based auto-generated key
data = {"name": "Tony Jason Charles"}
db.child("users").push(data)

data = {
    "name": "Mario",
    "email": "test@gmail.com"
}
db.child("other").push(data)

# Custom key
db.child("other").child("customkey").set(data)


# Update data

# Update data at single location
db.child("other").child("customkey").update({"name": "Jean"})

# Update data at multi-location
data = {
    "other/-MKOMLttrv2jM2gIy2g-/" : {
        "name": "John",
        "email": "test123@gmail.com"
    },
    "other/customkey/": {
        "name": "Henry",
        "email": "test456@gmail.com"
    }
}
db.update(data)


# Delete Data
db.child("users").child("-MKOLyp0-oAUiYUlFcUq").remove()


# Read Data
other = db.child("other").get()
for item in other.each():
    # print(item.key())
    # print(item.val())
    print(item.val()['email'])
    print(item.val()['name'])