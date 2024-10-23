### the following three lines are used for SSL problem on some computers.
### do NOT forget to add the following three lines to your code if you want to download something from the Internet
import certifi
import os
os.environ['SSL_CERT_FILE'] = certifi.where()

import firebase_admin
from firebase_admin import db, storage

### You need to download your own service account key file and store it together with your PY files
cred_obj = firebase_admin.credentials.Certificate('serviceAccountKey.json')

### Check the database URL and storage URL from your Firebase console
### Replace the databaseURL and storageBucket with your owns
firebase_admin.initialize_app(cred_obj, {
	'databaseURL':'https://comp7510-d77b7-default-rtdb.firebaseio.com/',
    'storageBucket':'comp7510-d77b7.appspot.com'
})

### Get a reference that refers to the root of your real-time database
db_ref = db.reference('/')
bucket = storage.bucket()

# Task3.1 - download and print usernames in the terminal
path = 'users'
data = db_ref.child(path).get()
for key in data.keys():
    print(f'Task3.1 - username - {key}')

# Task3.2 - download data of Bo Xiaoyu and print downloaded data in the terminal
path = 'users/bxy'
data = db_ref.child(path).get()
print(f'Task3.2 - Data downloaded from Bo Xiaoyu:')
print(data)
