from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import UserInfo
from .forms import UserForm
# ユーザ情報を辞書に格納して、users.htmlに返す
def showUsers(request):
    usefinfo = UserInfo.objects.all()
    context = {
        'msg': '現在の利用状況',
        'userinfo': usefinfo,
        'count':usefinfo.count,
    }
    
    return render(request, 'form/users.html',context)

def showDetail(request,user):
    #URLのidをもとに、ユーザ情報を抽出
    userinfoDetail = get_object_or_404(UserInfo,userName=user)
 
    context = {
        'userinfoDetail':userinfoDetail,
    }
    #detail.htmlへデータを渡す
    return render(request, 'form/detail.html',context)

def showCreateUserForm(request):
    #フォームを変数にセット
    form = UserForm()
 
    context = {
        'userForm':form,
    }
 
    #detail.htmlへデータを渡す
    return render(request, 'form/create.html',context)

def addUsers(request):
    if request.method=='POST':
        userForm = UserForm(request.POST)
        if(userForm.is_valid()):
            userForm.save()
    userinfo = UserInfo.objects.all()
    context = {
        'msg': '現在の利用状況',
        'userinfo': userinfo,
        'count':userinfo.count,
    }
    #user.htmlへデータを渡す
    return render(request, 'form/users.html',context)

def showEditUserForm(request,user):
 
    #idをもとにユーザ情報を取得
    userinfo = get_object_or_404(UserInfo,userName=user)
    #フォームをオブジェクトを作成
    userForm = UserForm(instance=userinfo)
    #ユーザ情報をフォームに格納
    context = {
        'userinfo':userinfo,
        'userForm':userForm,
    }
 
    #user.htmlへデータを渡す
    return render(request, 'form/edit.html',context)

def updateUser(request,user):
    if request.method=='POST':
        userInfo = get_object_or_404(UserInfo,userName=user)
        userForm = UserForm(request.POST,instance=userInfo)
        if userForm.is_valid():
            userForm.save()

    usefinfo = UserInfo.objects.all()
    context = {
        'msg': '現在の利用状況',
        'userinfo': usefinfo,
        'count':usefinfo.count,
    }
    #detail.htmlへデータを渡す
    return render(request, 'form/users.html',context)