from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


# Create your views here.
from crudapp.forms import LoginForm, StudentForm, BookForm
from crudapp.models import Student, Login, Book


def home(request):
    return render(request,'home.html')
def loginview(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        password = request.POST.get('pass')
        user= authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('adminhome')
            elif user.is_student:
                return redirect('studenthome')
        else:
         messages.info(request,'invalid credentials')
    return render(request,'login.html')
def adminview(request):
    return render(request,'adminhome.html')
def studenthome(request):
    return render(request,'studenthome.html')
def studentregister(request):
    login_form=LoginForm()
    student_form=StudentForm()
    if request.method =='POST':
        login_form = LoginForm(request.POST)
        student_form=StudentForm(request.POST)
        if login_form.is_valid() and student_form.is_valid():
            user= login_form.save(commit=False)
            user.is_student=True
            user.save()
            s=student_form.save(commit=False)
            s.user= user
            s.save()
            messages.info(request,'student registered successfully')
            return redirect('studentview')
    return render(request,'studentregister.html',{'login_form':login_form,'student_form':student_form})
def studentview(request):
    stud=Student.objects.all()
    return render(request,'studentview.html',{'stud':stud})
def studentupdate(request,id):
    stud=Student.objects.get(id=id)
    s=Login.objects.get(student=stud)
    if request.method == 'POST':
        form=StudentForm(request.POST or None,instance=stud)
        login_form=LoginForm(request.POST or None,instance=s)
        if form.is_valid() and login_form.is_valid():
            form.save()
            login_form.save()
            messages.info(request,'student updated successfully')
            return redirect('studentview')
    else:
        form=StudentForm(instance=stud)
        login_form=LoginForm(instance=s)
    return render(request,'studentupdate.html',{'form':form,'login_form':login_form})
def studentdelete(request,id):
    stud=Student.objects.get(id=id)
    s=Login.objects.get(student=stud)
    if request.method=='POST':
        s.delete()
        return redirect('studentview')
    else:
        return redirect('studentview')
def logoutview(request):
    logout(request)
    return redirect('loginview')
def BookAdd(request):
    form=BookForm()
    if request.method =='POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('BookView')
    return render(request,'BookAdd.html',{'form':form})
def BookView(request):
    Bk =Book.objects.all()
    return render(request,'BookView.html',{'Bk':Bk})
def BookUpdate(request,idb):
    bk=Book.objects.get(id=idb)

    if request.method=='POST':
        form=BookForm(request.POST or None,instance=bk)
        if form.is_valid():
            form.save()
            messages.info(request,'Book updated successfully')
            return redirect('BookView')
    else:
        form=BookForm(instance=bk)
    return render(request,'BookUpdate.html',{'form':form})
def Bookdelete(request,idb):
    if request.method=='POST':
        dbk=Book.objects.get(id=idb)
        dbk.delete()
        return redirect('BookView')







