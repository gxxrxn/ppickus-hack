from django.shortcuts import render,redirect
from .models import Users
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

ERROR_MSG = {
    'ID_EXIST': '이미 사용 중인 아이디 입니다.',
    'ID_NOT_EXIST': '존재하지 않는 아이디 입니다.',
    'ID_PW_MISSING': '아이디와 비밀번호를 확인해주세요.',
    'PW_CHECK': '비밀번호가 일치하지 않습니다.'
}

def index(request):
    context = {'a':1}
    return render(request, 'index.html', context)

def hotel(request):
    context = {'a':1}
    return render(request, 'hotel.html', context)

def vr(request):
    context = {'a':1}
    return render(request, 'vr.html', context)

def display(request):
    context = {'a':1}
    return render(request, 'display.html', context)

def leisure(request):
    context = {'a':1}
    return render(request, 'leisure.html', context)

def show(request):
    context = {'a':1}
    return render(request, 'show.html', context)

def video(request):
    context = {'a':1}
    return render(request, 'video.html', context)

def tour(request):
    context = {'a':1}
    return render(request, 'tour.html', context)

def register(request):
    context = {
        'error':{
            'state':False,
            'msg':''

        }
    }
    return render(request, 'register.html', context) 

def login(request):
     
    context = {
        'error':{
            'state':False,
            'msg':''

        }
    }

    if request.method =='POST':
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']

        user = User.objects.filter(username=user_id)

        if (user_id and user_pw):
            if len(user) != 0:
                user = auth.authenticate(
                    username = user_id,
                    password = user_pw
                )

                if user != None:
                    auth.login(request, user)

                    return redirect('index')
                    
                else:
                    context['error']['state'] = True
                    context['error']['msg'] = ERROR_MSG['PW_CHECK']
            else:
                context['error']['state'] = True
                context['error']['msg'] = ERROR_MSG['ID_NOT_EXIST']
        else:
            context['error']['state'] = True
            context['error']['msg'] = ERROR_MSG['ID_PW_MISSING']

    return render(request, 'login.html', context)

def logout(request):
    auth.logut(request)
    return render(request,'index.html')

