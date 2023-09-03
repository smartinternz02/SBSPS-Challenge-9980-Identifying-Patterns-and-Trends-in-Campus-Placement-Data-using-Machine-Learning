from django.shortcuts import render,redirect
import pyrebase
from django.contrib.auth import authenticate, login
from django.contrib import messages
from . import forms
from firebase_admin import firestore
import pyrebase
import os
import firebase_admin
from firebase_admin import credentials,firestore
import prepcamp.settings as config
import base.mba as mba
import base.engg as engg
import base.faculty_engg as faculty_engg
import base.faculty_mba as faculty_mba
db=config.db
# from .forms import studentloginForm,studentRegistrationForm
# Create your views here.
Config = {
    "apiKey": "AIzaSyDDBU8CKyWSAHnutcdSHqYDQrxVr01FzNE",
    "authDomain": "prepcamp-2d11b.firebaseapp.com",
    "databaseURL": "https://prepcamp-2d11b-default-rtdb.firebaseio.com",
    "projectId": "prepcamp-2d11b",
    "storageBucket": "prepcamp-2d11b.appspot.com",
    "messagingSenderId": "369015653140",
    "appId": "1:369015653140:web:deca38edc029c0fc19b801"
  }
firebase=pyrebase.initialize_app(Config)
auth=firebase.auth()
database=firebase.database()
# json_file_path = os.path.join('./prepcamp-2d11b-firebase-adminsdk-jol63-64d1c726d5.json')
# cred = credentials.Certificate(json_file_path)
# firebase_admin.initialize_app(cred)
# firebase = pyrebase.initialize_app(Config)
# auth = firebase.auth()
# db=firestore.client()
#---------------------Landing Page-------------------------------
def landing(request):
    return render(request,'base/landing.html')

#-----------------------Home Page--------------------------------
def home_mba(request):
    return render(request,'base/index.html')

def home_engg(request):
    return render(request,'base/index_engg.html')
# --------------------Student LoginPage-------------------
def studentsignup_mba(request):
    if request.method=="GET":
        return render(request,"base/studentlogin.html")
    if request.method=="POST":
        print('Inside the method post')
        name=request.POST.get('studentname')
        # print(name)
        emailid=request.POST.get('studentemail')
        password=request.POST.get('studentpassword')
        print("@@@@@@@@@@")
        print(name,emailid,password)
        # name=database.child('Data').child('Name').get().val()
        # emailid=database.child('Data').child('Emailid').get().val()
        # password=database.child('Data').child('Password').get().val()
        print("************")
        print(name,emailid,password)
        print("************")

        user=auth.create_user_with_email_and_password(emailid,password)
        print(user)
        uid=user['localId']
        request.session['uid']=str(uid)
        user_doc_ref = db.collection('Students').document(uid)
        user_doc_ref.set({
                'name': name,
                'email': emailid,
                'Mba_Skills':[],
                'Engg_Skills':[]
            })
        # print(uid)
        return render(request,"base/studentlogin.html")
    # data={"name":name}
    #     database.child('Data').child('Name').set(data)

def studentsignup_engg(request):
    if request.method=="GET":
        return render(request,"base/studentlogin_engg.html")
    if request.method=="POST":
        print('Inside the method post')
        name=request.POST.get('studentname')
        # print(name)
        emailid=request.POST.get('studentemail')
        password=request.POST.get('studentpassword')
        print("@@@@@@@@@@")
        print(name,emailid,password)
        # name=database.child('Data').child('Name').get().val()
        # emailid=database.child('Data').child('Emailid').get().val()
        # password=database.child('Data').child('Password').get().val()
        print("************")
        print(name,emailid,password)
        print("************")

        user=auth.create_user_with_email_and_password(emailid,password)
        print(user)
        uid=user['localId']
        request.session['uid']=str(uid)
        user_doc_ref = db.collection('Students').document(uid)
        user_doc_ref.set({
                'name': name,
                'email': emailid,
                'Mba_Skills':[],
                'Engg_Skills':[]
            })
        # print(uid)
        return render(request,"base/studentlogin_engg.html")

def studentlogin_mba(request):
        if request.method == 'GET':
             return render(request,"base/studentlogin.html")
        if request.method == 'POST':
            try:
                print("We are inside the login")
                emailid=request.POST.get('studentemail')
                password=request.POST.get('studentpassword')
                print("Inside the login option")
                print('-----------------------------')
                print(emailid,password)
                print('-----------------------------')
                user=auth.sign_in_with_email_and_password(emailid,password)
                uid=user['localId']
                request.session['uid']=str(uid)
                print("User is this",user)

            except:
                print("invalid Credintials") 

            session_id = user['localId']
            request.session['uid']=str(session_id)
            return render(request,'base/studentdashboard.html') 


def studentlogin_engg(request):
         if request.method == 'GET':
             return render(request,"base/studentlogin_engg.html")
         if request.method== 'POST':
            try:
                emailid=request.POST.get('studentemail')
                password=request.POST.get('studentpassword')
                print("Inside the login option")
                print('-----------------------------')
                print(emailid,password)
                print('-----------------------------')
                user=auth.sign_in_with_email_and_password(emailid,password)
                uid=user['localId']
                request.session['uid']=str(uid)
                print(user)

            except:
                print("invalid Credintials") 

            session_id = user['localId']
            request.session['uid']=str(session_id)
            return render(request,'base/studentdashboard_engg.html') 
#-------------------Student Dashboard Page-------------------------
def studentdashboard_mba(request):
    return render(request,"base/studentdashboard.html")

def student_enggDashboard(request):
    return render(request,"base/studentdashboard_engg.html")

#--------------------Faculty Signup Page-----------------------
def facultysignup_mba(request):
    # if request.method=="GET":
    #     print("inside login for the faculty")
    #     return render(request,"base/facultylogin.html")
    # if request.method=="POST":
        print('Inside the faculty method post')
        name=request.POST.get('facultyname')
        emailid=request.POST.get('facultyemail')
        password=request.POST.get('facultypassword')
        print("@@@@@@@@@@")
        print(name,emailid,password)
        
        print("************")
        print(name,emailid,password)
        print("************")

        User=auth.create_user_with_email_and_password(emailid,password)
        print(User)
        uid=User['localId']
        user_doc_ref = db.collection('Faculty').document(uid)
        user_doc_ref.set({
                'name': name,
                'email': emailid,
                'Mba_Skills':[],
                'Engg_Skills':[]
            })
        print(uid)
        return render(request,"base/facultylogin.html")
        # data={"name":name}
        # database.child('Data').child('Name').set(data)
        # return "hello"

#--------------------Faculty Login  Page-----------------------
def facultylogin_mba(request):
        if request.method=='GET' :
             return render (request , "base/facultylogin.html")
        if request.method == 'POST':
            try:
                
                    emailid=request.POST.get('facultyemail')
                    password=request.POST.get('facultypassword')
                    print("Inside the login option")
                    print('-----------------------------')
                    print(emailid,password)
                    print('-----------------------------')
                    User=auth.sign_in_with_email_and_password(emailid,password)
                    print(User)
                    session_id = User['idToken']
                    request.session['uid']=str(session_id)

            except:
                print("invalid Credintials") 

            
            return render(request,'base/facultydashboard.html')  

def facultysignup_engg(request):
    if request.method=="GET":
        print("inside login for the faculty")
        return render(request,"base/facultylogin_engg.html")
    if request.method=="POST":
        print('Inside the engg faculty method post')
        name=request.POST.get('facultyname')
        emailid=request.POST.get('facultyemail')
        password=request.POST.get('facultypassword')
        print("@@@@@@@@@@")
        print(name,emailid,password)
        
        print("************")
        print(name,emailid,password)
        print("************")

        User=auth.create_user_with_email_and_password(emailid,password)
        print(User)
        uid=User['localId']
        user_doc_ref = db.collection('Faculty').document(uid)
        user_doc_ref.set({
                'name': name,
                'email': emailid,
                'Mba_Skills':[],
                'Engg_Skills':[]
            })
        print(uid)
        return render(request,"base/facultylogin_engg.html")
def facultylogin_engg(request):
        if request.method=="GET":
            print("inside login for the faculty")
            return render(request,"base/facultylogin_engg.html")
        if request.method == "POST":
            try:
                
                    emailid=request.POST.get('facultyemail')
                    password=request.POST.get('facultypassword')
                    print("Inside the engg login option")
                    print('-----------------------------')
                    print(emailid,password)
                    print('-----------------------------')
                    User=auth.sign_in_with_email_and_password(emailid,password)
                    print(User)
                    session_id = User['idToken']
                    request.session['uid']=str(session_id)

            except:
                print("invalid Credintials") 

            
            return render(request,'base/facultydashboard_engg.html')                                                         

#-------------------Faculty Dashboard Page-------------------------
def facultydashboard(request):
        return render(request,"base/facultydashboard.html")
    # if request.method == 'POST':
        # file = request.files['file'] # fet input
        # filename = file.filename      
        # print("@@ Input posted = ", filename)
        
        # file_path = os.path.join('static/upload', filename)
        # file.save(file_path)
        # print('Inside the POST')
        # print(file_path)
        # return render(request,"base/facultydashboard.html")

def facultydashboard_engg(request):
    # if request.method == 'GET':
        return render(request,"base/facultydashboard_engg.html")

def csvupload_engg(request):
     if request.method=='GET':
          return render(request,"base/csvupload_engg.html")
     if request.method=='POST':
        file =  request.FILES['file']# fet input
        with open('base/upload/'+file.name, 'wb+') as destination:  
            for chunk in file.chunks():  
                destination.write(chunk)  
        # filename = file.filename      
        # print("@@ Input posted = ", filename)
        
        # file_path = os.path.join('base/upload', filename)
        # file.save(file_path)
        # print('Inside the POST')
        # print(file_path)

        engg_clust=faculty_engg.engg_clusters('base/upload/'+file.name)
        engg_place=faculty_engg.engg_place('base/upload/'+file.name)

        idtoken = request.session['uid']
        UpdateInfo = {
            'engg_placement':engg_place[0]
        }
        StudRef = db.collection('Faculty').document(idtoken)
        print(UpdateInfo)
        try:
            StudRef.update({"Engg_Skills": firestore.ArrayUnion([UpdateInfo])})
            print('Hello')
        except:
            print('Error in uploading')

       
        return render(request,"base/eng_result.html",{'clust0':engg_clust[0],'clust1':engg_clust[1],'clust2':engg_clust[2],'clust3':engg_clust[3],'clust4':engg_clust[4],'place':engg_place[0]})

def csvupload_mba(request):
     if request.method=='GET':
          return render(request,"base/csvupload_mba.html")
     if request.method=='POST':
        file =  request.FILES['file']# fet input
        with open('base/upload/'+file.name, 'wb+') as destination:  
            for chunk in file.chunks():  
                destination.write(chunk) 
     
        mba_clusters=faculty_mba.clusters('base/upload/'+file.name)
        mba_placement=faculty_mba.placement_status('base/upload/'+file.name)
        mba_salary=faculty_mba.salary('base/upload/'+file.name)

        idtoken = request.session['uid']
        UpdateInfo = {
            'mba_placement':mba_placement[1]
        }
        StudRef = db.collection('Faculty').document(idtoken)
        print(UpdateInfo)
        try:
            StudRef.update({"Mba_Skills": firestore.ArrayUnion([UpdateInfo])})
            print('Hello')
        except:
            print('Error in uploading')
        return render(request,"base/mba_result.html",{'clust':mba_clusters,'perc':mba_placement[1],'salary':mba_salary})        
    # if request.method=='POST':

    #     file = request.files['file'] # fet input
    #     filename = file.filename      
    #     print("@@ Input posted = ", filename)
        
    #     file_path = os.path.join('static/upload', filename)
    #     file.save(file_path)
    #     print('Inside the POST')
    #     print(file_path)
    #     return render(request,"base/facultydashboard.html")
                                            
        
# def engg_form(request):
#     if request.method == "GET":
#         return render(request,"engineeringform.html")
#     if request.method == "POST":
#         gender=request.POST.get('gender')
#         age = request.POST.get('Age')
#         hsc_p=request.POST.get('hsc_p')
#         Internships=request.POST.get("Internships")
#         CGPA = request.POST.get("CGPA")
#         HistoryOfBacklogs=request.POST.get("HistoryOfBacklogs")
#         Hostel=request.POST.get("Hostel")
#         Stream=request.POST.get("Stream")

def engg_form(request):
    if request.method == "GET":
        return render(request,"base/engineeringform.html")
    if request.method=="POST":
        Gender=request.POST.get('gender')
        Age=request.POST.get("Age")
        Internships=request.POST.get("Internships")
        CGPA=request.POST.get("CGPA")
        HistoryOfBacklogs=request.POST.get("HistoryOfBacklogs")
        Hostel=request.POST.get("Hostel")
        Stream=request.POST.get("Stream")

        engg_clust=engg.engg_clusters(Age,Gender,Stream,Internships,CGPA,Hostel,HistoryOfBacklogs)
        engg_place=engg.engg_place(Age,Gender,Stream,Internships,CGPA,Hostel,HistoryOfBacklogs)

        idtoken = request.session['uid']
        UpdateInfo = {
            'Gender':Gender,
            'Age':Age,
            'Intenrships':Internships,
            'CGPA':CGPA, 
            'HistoryOfBacklogs':HistoryOfBacklogs,
            'Hostel':Hostel,
            'Stream':Stream,
            'engg_placement':engg_place[0]
        }
        StudRef = db.collection('Students').document(idtoken)
        print(UpdateInfo)
        try:
            StudRef.update({"Engg_Skills": firestore.ArrayUnion([UpdateInfo])})
            print('Hello')
        except:
            print('Error in uploading')

       
        return render(request,"base/eng_result.html",{'clust0':engg_clust[0],'clust1':engg_clust[1],'clust2':engg_clust[2],'clust3':engg_clust[3],'clust4':engg_clust[4],'place':engg_place[0]})

# def engg_result(request):
#      return render(request,"base/eng_result.html")        

def mba_form(request):
    if request.method == "GET":
        return render(request,"base/mbaform.html")
    if request.method == "POST":
        gender=request.POST.get('gender')
        ssc_p=request.POST.get("ssc_p")
        ssc_b=request.POST.get("ssc_b")
        hsc_p =request.POST.get("hsc_p")
        hsc_b=request.POST.get("hsc_b")
        hsc_s=request.POST.get("hsc_s")
        degree_p=request.POST.get("degree_p")
        degree_t=request.POST.get("degree_t")
        workex=request.POST.get("workex")
        etest_p=request.POST.get("etest_p")
        specialisation=request.POST.get("specialisation")
        mba_p=request.POST.get("mba_p")

        # print(gender,ssc_p,ssc_b,hsc_b,hsc_s,degree_p,degree_t,workex,etest_p,specialisation,mba_p)
        print(gender)
        print(int(ssc_p))
        print(ssc_b)
        print(hsc_b)
        print(hsc_s)
        print(int(degree_p))
        print(degree_t)
        print(workex)

        idtoken = request.session['uid']
        
        print(int(etest_p))
        print(specialisation)
        print(int(mba_p))

        
        mba_clusters=mba.clusters(gender,int(ssc_p),ssc_b,int(hsc_p),hsc_b,hsc_s,int(degree_p),degree_t,workex,int(etest_p),specialisation,int(mba_p))
        mba_placement=mba.placement_status(gender,int(ssc_p),ssc_b,int(hsc_p),hsc_b,hsc_s,int(degree_p),degree_t,workex,int(etest_p),specialisation,int(mba_p))
        mba_salary=mba.salary(gender,int(ssc_p),ssc_b,int(hsc_p),hsc_b,hsc_s,int(degree_p),degree_t,workex,int(etest_p),specialisation,int(mba_p))

        UpdateInfo = {
            'gender':gender,
            'ssc_p':ssc_p,
            'ssc_b':ssc_b,
            'hsc_p':hsc_p, 
            'hsc_b':hsc_b,
            'hsc_s':hsc_s,
            'degree_p':degree_p,
            'degree_t':degree_t,
            'workex':workex,
            'etest_p':etest_p,
            'specialisation':specialisation,
            'mba_p':mba_p,
            'mba_placement':mba_placement[1]
        }
        StudRef = db.collection('Students').document(idtoken)
        print(UpdateInfo)
        try:
            StudRef.update({"Mba_Skills": firestore.ArrayUnion([UpdateInfo])})
            print('Hello')
        except:
            print('Error in uploading')
        print(mba_clusters[0])
        return render(request,"base/mba_result.html",{'clust0':mba_clusters[0],'clust1':mba_clusters[1],'clust2':mba_clusters[2],'clust3':mba_clusters[3],'clust4':mba_clusters[4],'perc':mba_placement[1],'salary':mba_salary})

def mba_result(request):
     return render(request,"base/mba_result.html")        



# def uploadcsv(request):
#   if request.method == 'GET':
#     form = csvupload()
#     return render(request, 'base/csv_upload.html', {'form':form})

#   # If not GET method then proceed
#   try:
#     form = csv_upload(data=request.POST, files=request.FILES)
#     if form.is_valid():
#       csv_file = form.cleaned_data['csv_file']
#     if not csv_file.name.endswith('.csv'):
#       messages.error(request, 'File is not CSV type')
#       return redirect('base/landing.html')
#     # If file is too large
#     if csv_file.multiple_chunks():
#       messages.error(request, 'Uploaded file is too big (%.2f MB)' %(csv_file.size(1000*1000),))
#       return redirect('base/landing.html')
    
#     file_data = csv_file.read().decode('utf-8')
#     lines = file_data.split('\n')

#     # loop over the lines and save them in db. If error, store as string and then display
#     for line in lines:
#       fields = line.split(',')
#       data_dict = {}
#       print(data_dict)
#       try:
#         form = csv_upload(data_dict)
#         if form.is_valid():
#           form.save()
#         else:
#           logging.getLogger('error_logger').error(form.errors.as_json())
#       except Exception as e:
#         logging.getLogger('error_logger').error(form.errors.as_json())
#         pass
#   except Exception as e:
#     logging.getLogger('error_logger').error('Unable to upload file. ' + repr(e))
#     messages.error(request, 'Unable to upload file. ' + repr(e))
#   return redirect('base/facultydashboard_engg.html')


   
