from multiprocessing import context
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
import pyrebase 
from firebase_admin import credentials  # type: ignore
cred = credentials.Certificate('firebase_admin.json')
firebase_admin.initialize_app(cred)



config={
    "apiKey": "AIzaSyCrpyAgkJXzIZ_ij8fd4eYdSOna8aPO1G0",
    "authDomain": "rfid-fbe6a.firebaseapp.com",
    "databaseURL": "https://rfid-fbe6a-default-rtdb.firebaseio.com",
    "projectId": "rfid-fbe6a",
    "storageBucket": "rfid-fbe6a.appspot.com",
    "messagingSenderId": "956156149917",
    "appId": "1:956156149917:web:25f6d76eb2081b80d8d474",
    
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

def home(request):
    return render(request,'home.html')
def read(request):
    return render(request,'read.html')
def read1(request):
    name=database.child('data').child('name').get().val()
    batchno=database.child('data').child('batchno').get().val()
    modelno=database.child('data').child('modelno').get().val()
    sourceaddress=database.child('data').child('source').get().val()
    destinationaddress=database.child('data').child('destination').get().val()
    packeddate=database.child('data').child('packed').get().val()
    expirydate=database.child('data').child('expiry').get().val()
    placeoforigin=database.child('data').child('place').get().val()
    no_of_quantity=database.child('data').child('no').get().val()
    tagid=database.child('data').child('tagid').get().val()
    placeofarriving=database.child('data').child('arriving').get().val()
    alert=database.child('data').child('arriving').get().val()
    cur=database.child('data').child('cur').get().val()
    min=database.child('data').child('min').get().val()
    max=database.child('data').child('max').get().val()
    return render(request,'read1.html',{
        "cur":cur,
        "max":max,
        "min":min,
        "alert":alert,
        "name":name,
        "batchno":batchno,
        "modelno":modelno,
        "sourceaddress":sourceaddress,
        "destinationaddress":destinationaddress,
        "packeddate":packeddate,
        "expirydate":expirydate,
        "placeoforigin":placeoforigin,
        "no_of_quantity":no_of_quantity,
        "tagid":tagid,
        "placeofarriving":placeofarriving
    })
def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            # Verify user credentials
            user = auth.get_user_by_email(email)
            if user.email == email and user.password == password:
                # Sign in the user
                user = auth.sign_in_with_email_and_password(email, password)
                messages.success(request, 'User signed in successfully.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid email or password.')
        except Exception as e:
            messages.error(request, str(e))

    return render(request, 'signin.html')
def register1(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['user']
        password = request.POST['pass']
        try:
            user_data={
            "username": username,
            "password": password,
            "email": email
            }
            database.child('signup').push(user_data)
            return redirect('/home')
        except Exception as e:
            error_message=str(e)
            return render(request,'signup.html',{'error':error_message})
    
    else:
        return render(request,'signup.html')
def signup(request):
    return render(request,'signup.html')
def register_w1(request):
    if request.method == 'POST':
        prname = request.POST['prname']
        batchno = request.POST['batchno']
        modelno =request.POST['modelno']
        quantity = request.POST['quantity']
        maname = request.POST['maname']
        user2={
            "prname":prname,
            "batchno":batchno,
            "modelno":modelno,
            "quantity":quantity,
            "maname":maname
        }
        database.child('user').push(user2)
        return redirect('/write2')
    else:
        return render(request,'write.html')
def register_w2(request):
    if request.method == 'POST':
        saddress = request.POST['saddress']
        daddress = request.POST['daddress']
        mdate =request.POST['mdate']
        edate = request.POST['edate']
        maxtemp = request.POST['maxtemp']
        mintemp = request.POST['mintemp']
        user3={
            "saddress":saddress,
            "daddress":daddress,
            "mdate":mdate,
            "edate":edate,
            maxtemp:mintemp,
            mintemp:mintemp,

        }
        database.child('user').push(user3)
        return redirect('/home')
    return render(request,'write2.html')
def track(request):
    return render(request,'track.html')

def track2(request):
 
    number=database.child('data2').child('number').get().val()
    source=database.child('data2').child('source').get().val()
    destination=database.child('data2').child('destination').get().val()
    source1=database.child('data2').child('source1').get().val()
    deg=database.child('data2').child('deg').get().val() 
    time=database.child('data2').child('time').get().val() 
    source2=database.child('data2').child('source2').get().val()
    deg2=database.child('data2').child('deg2').get().val() 
    time2=database.child('data2').child('time2').get().val()
    source3=database.child('data2').child('source3').get().val()
    deg3=database.child('data2').child('deg3').get().val() 
    time3=database.child('data2').child('time3').get().val()  
    data =[
        {"source1":source1,
        "deg":deg,
        "time":time},
        {"source1":source2,
         "deg":deg2,
         "time":time2},
        {"source1":source3,
         "deg":deg3,
         "time":time3},
     
    ]
    context={
        'data':data,
        "number":number,
        "source":source,
        "destination":destination,

    }
    return render(request,'track2.html',context=context)

# Create your views here.
