from django.shortcuts import render, redirect
from .form import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, HttpResponseRedirect
import random
import string
from django.contrib.auth.decorators import login_required


def admission_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))


def register(request):
    if request.method == 'POST':
        ak = signup(request.POST)
        if ak.is_valid():
            ak.save()
            return HttpResponseRedirect('/login')
        else:
            return HttpResponse('error')
    else:
        ak = signup()
        return render(request, 'register.html', {'ak': ak})


# login
def bogin(request):
    if request.method=='POST':
        ak = AuthenticationForm(request=request,data=request.POST)
        if ak.is_valid ():
            name = ak.cleaned_data.get('username')
            password = ak.cleaned_data.get('password')
            user = authenticate(username=name,password=password)
            if user is not None:
                login(request,user)
                return redirect('/tlist')
        else:
            return HttpResponse('/login')
    else:

        gm = AuthenticationForm()
        return render(request,'login.html',{'rm':gm})

# logout
@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    return render(request,'logout.html')

# Create your views here.
def teacherlist(request):
    ab = teacher.objects.all()
    return render(request, 'teacherlist.html', {'ab': ab})


@login_required(login_url='/login')
def teacheradd(request):
    if request.method == 'POST':
        ak = teacherplus(request.POST)
        if ak.is_valid():
            name = ak.cleaned_data.get('tname')
            address = ak.cleaned_data.get('address')
            mobile = ak.cleaned_data.get('mobile')
            subject = ak.cleaned_data.get('subject')
            up = teacher(tname=name, teacherid=admission_id(), subject=subject, address=address, mobile=mobile)
            up.save()
            return HttpResponseRedirect('/tlist')
        else:
            return HttpResponse('error')
    else:
        ak = teacherplus()
        return render(request, 'teacheradd.html', {'ak': ak})


@login_required(login_url='/login')
def teacherupdate(request, id):
    ab = teacher.objects.get(pk=id)
    if request.method == 'POST':
        ak = teacherplus(request.POST, instance=ab)
        if ak.is_valid():
            name = ak.cleaned_data.get('tname')
            address = ak.cleaned_data.get('address')
            mobile = ak.cleaned_data.get('mobile')
            subject = ak.cleaned_data.get('subject')
            up = teacher(id=id,tname=name, teacherid=admission_id(), subject=subject, address=address, mobile=mobile)
            up.save()
            return HttpResponseRedirect('/tlist')
        else:
            return HttpResponse('error')
    else:
        ak = teacherplus(instance=ab)
        return render(request, 'teacheradd.html', {'ak': ak})


@login_required(login_url='/login')
def teacherdelete(request, name):
    ab = teacher.objects.get(tname=name)
    ab.delete()
    return HttpResponseRedirect('/tlist')


def studentlist(request):
    ab = student.objects.all()
    return render(request, 'studentlist.html', {'ab': ab})


@login_required(login_url='/login')
def studentadd(request):
    if request.method == 'POST':
        ak = studentplus(request.POST)
        if ak.is_valid():
            name = ak.cleaned_data.get('name')
            classe = ak.cleaned_data.get('classe')
            address = ak.cleaned_data.get('address')
            mother = ak.cleaned_data.get('mother')
            father = ak.cleaned_data.get('father')
            mobile = ak.cleaned_data.get('mobile')
            roll = ak.cleaned_data.get('roll')
            up = student(name=name, admissionid=admission_id(), roll=roll, classe=classe, address=address,
                         mother=mother, father=father, mobile=mobile)
            up.save()
            return redirect('/')
        else:
            return HttpResponse('error')
    else:
        ak = studentplus()
        return render(request, 'studentadd.html', {'ak': ak})


@login_required(login_url='/login')
def studentupdate(request, id):
    ab = student.objects.get(pk=id)
    if request.method == 'POST':
        ak = studentplus(request.POST, instance=ab)
        if ak.is_valid():
            name = ak.cleaned_data.get('name')
            classe = ak.cleaned_data.get('classe')
            address = ak.cleaned_data.get('address')
            mother = ak.cleaned_data.get('mother')
            father = ak.cleaned_data.get('father')
            mobile = ak.cleaned_data.get('mobile')
            roll = ak.cleaned_data.get('roll')
            up = student(id=id,roll=roll,name=name,admissionid=admission_id(), classe=classe, address=address, mother=mother, father=father, mobile=mobile)
            up.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('error')
    else:
        ak = studentplus(instance=ab)
        return render(request, 'studentupdate.html', {'ak': ak})


@login_required(login_url='/login')
def studentdelete(request, name):
    ab = student.objects.get(name=name)
    ab.delete()
    return HttpResponseRedirect('/')
