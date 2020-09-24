from django.shortcuts import render,redirect
from .models import Users
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Users, Categories, Videos

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
    # hotel에 해당하는 객체만 가져온다
    hotel_obj = Categories.objects.get(pk=1)
    video_obj = Videos.objects.filter(pacticipate_category=hotel_obj).values()
    
    print(video_obj[5]['thumb_path'])

    context = {}

    for i in range(1, 8):
        context[f'{i}_video_path'] = video_obj[i-1]['video_path'] + '.mp4'
        context[f'{i}_thumb_path'] = video_obj[i-1]['thumb_path'] + '.jpg'
        context[f'{i}_video_name'] = video_obj[i-1]['video_name']
        context[f'{i}_video_explain'] = video_obj[i-1]['video_explain']

    
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
    show_obj = Categories.objects.get(pk=5)
    video_obj = Videos.objects.filter(pacticipate_category=show_obj).values()
    
    context = {}

    print(video_obj[3]['video_path'])

    for i in range(1, 8):
        context[f'{i}_video_path'] = video_obj[i-1]['video_path'] + '.mp4'
        context[f'{i}_thumb_path'] = video_obj[i-1]['thumb_path'] + '.jpg'
        context[f'{i}_video_name'] = video_obj[i-1]['video_name']
        context[f'{i}_video_explain'] = video_obj[i-1]['video_explain']

    return render(request, 'show.html', context)

def video(request):
    context = {'a':1}
    return render(request, 'video.html', context)

def tour(request):
    context = {'a':1}
    return render(request, 'tour.html', context)

def mypage(request):
    context = {'a':1}
    return render(request, 'mypage.html', context)

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
    auth.logout(request)

    return render(request,'index.html')

def register(request):

    context = {
        'error': {
            'state': False,
            'msg': ''
        },
        'success': {
            'state': False
        }
    }

    if request.method == "POST":
        name = request.POST['user_name']
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']
        user_pw_check = request.POST['user_pw_check']
        user_email = request.POST['user_email']

        user = User.objects.filter(username=user_id)

        if len(user) == 0:
            if user_pw == user_pw_check:
                created_user = User.objects.create_user(
                    username=user_id,
                    password=user_pw
                )

                Users.objects.create(
                    user_name=name,
                    user_id=user_id,
                    user_pw=user_pw,
                    user_email=user_email
                )

                auth.login(request, created_user)
                context['success']['state'] = True

                return redirect('index')

            else:
                context['error']['state'] = True
                context['error']['msg'] = ERROR_MSG['PW_CHECK']
        else:
            context['error']['state'] = True
            context['error']['msg'] = ERROR_MSG['ID_EXIST']

    return render(request, 'register.html', context)

