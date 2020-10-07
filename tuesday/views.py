from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render, redirect
from .models import User, Employee, Investment
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


# Create your views here.

def login(request):
    # return HttpResponse('This is home')
    return render(request, 'front/login.html')


@login_required(login_url="/")
def home(request, **kwargs):
    allUsers = Employee.objects.all().order_by('-eid')
    context = {"allUsersdata": allUsers}
    return render(request, 'front/index.html', context)


def register(request):
    # return HttpResponse('This is home')
    # if request.method == "POST":
    #     username = request.POST['username']
    #     user = auth.authenticate(username=username)

    return render(request, 'front/register.html')


def userregister(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        # Check for error inputs
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name,
                                        last_name=last_name)
        user.save()
        messages.success(request, '<p class="success_login text-danger ">You were successfully login</p>')

        # messages.success(request, "Your Account has been successfully created !!")
        # return redirect('/')
        return render(request, 'front/register.html')


def userlogin(request):
    if request.method == "POST":
        # chack user
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect(home)
        else:
            return render(request, 'front/login.html', {'error': "Username and password not match"})

    else:
        return render(request, '/')


@login_required(login_url="/")
def addnew(request):
    return render(request, 'front/add_member.html')


def logout(request):
    auth.logout(request)
    return redirect("/")


@login_required(login_url="/")
def addnewdata(request):
    if request.method == "POST":
        ename = request.POST['ename']
        edate = request.POST['edate']
        eposition = request.POST['eposition']
        esallery = request.POST['esallery']
        eleft = request.POST['eleft']

        # Check for error inputs

        userdata = Employee(ename=ename, edate=edate, eposition=eposition, esallery=esallery, eleft=eleft)
        userdata.save()
        messages.success(request, "Your Account has been successfully created !!")
        return redirect(home)
        # return render(request, 'front/index.html')

    else:
        return HttpResponse('404 - Not Found')


@login_required(login_url="/")
def deletedata(request, eid):
    pi = Employee.objects.get(eid=eid)
    pi.delete()
    return redirect(home)


@login_required(login_url="/")
def edituser(request, eid):
    # return HttpResponse('This is home')
    gdata = Employee.objects.get(eid=eid)
    return render(request, 'front/edituser.html', {"gdata": gdata})


@login_required(login_url="/")
def updatedata(request, eid):
    if request.method == 'POST':
        student_obj = Employee.objects.get(eid=eid)
        student_obj.ename = request.POST['ename']
        student_obj.edata = request.POST['edate']
        student_obj.eposition = request.POST['eposition']
        student_obj.esallery = request.POST['esallery']
        student_obj.left = request.POST['eleft']
        student_obj.save()
        return redirect(home)




@login_required(login_url="/")
def investdata(request, eid):
    allInvest = Investment.objects.all()
    # context = {"allInvest": allInvest}
    gdata = Employee.objects.get(eid=eid)

    # getdata = Employee.objects.get(eid=eid)
    # context2 = {"getdata": getdata}
    return render(request, 'front/envesttable.html',  {"gdata": gdata})


def addnewinvest(request , id ):
    if request.method == "POST":
        invdate = request.POST['invdate']
        invpayd = request.POST['invpayd']
        invrs = request.POST['invrs']



        invdata = Investment(invdate=invdate, invpayd=invpayd, invrs=invrs)
        invdata.save()
        messages.success(request, "Your investment has been successfully created !!")
        return redirect(investdata)

    else:
        return HttpResponse('404 - Not Found')
