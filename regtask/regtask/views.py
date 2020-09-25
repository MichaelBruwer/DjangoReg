from django.shortcuts import render
#importing class RecordInsert from models.py
from regtask.models import RecordInsert
from django.contrib import messages

#Defineing insert request 
def Insertrecord(request):
    if request.method=='POST':
        #Telling func where to find info to post to db
        if request.POST.get('fname') and request.POST.get('lname') and request.POST.get('email') and request.POST.get('Type') and request.POST.get('username') and request.Post.get('password'):
            saverecord=RecordInsert()
            #temp storeing data in saferecord
            saverecord.fname=request.POST.get('fname')
            saverecord.lname=request.POST.get('lname')
            saverecord.email=request.POST.get('email')
            saverecord.type=request.POST.get('Type')
            saverecord.type=request.POST.get('username')
            saverecord.type=request.POST.get('password')
            #saveing all records stored in saverecored to database
            saverecord.save()
            #on success displaying message
            messages.success(request,'Record Saved Succesfully!!')
            return render(request,'Index.html')
        else: 
            return render(request,'Index.html')