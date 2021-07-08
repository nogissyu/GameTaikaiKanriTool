from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import UserInfo
from .models import battledata
from .models import Entry
from .forms import UserForm,dataForm, PlaierForm
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

def syouhaiForm(request):
    battleData = battledata.objects.all()
    context = {
        'battledata' : battleData,
    }
    return render(request, 'form/syouhaikai.html',context)

def syouriData(request,Id):
    if request.method == 'POST':
        Battledata = get_object_or_404(battledata,battleID=Id)
        if Battledata.winner != "none":
            context = {
                'battledata' : Battledata,
                }
            return render(request,'form/error.html',context)
        elif 'button1' in request.POST:
            Battledata.winner = Battledata.userID1
            Battledata.save()
            index="勝利"
        elif 'button2' in request.POST:
            Battledata.winner = Battledata.userID2
            Battledata.save()
            index="敗北"

    context = {
        'battledata' : Battledata,
        'index' : index,
    }
    return render(request, 'form/syouhaikekka.html',context)

def win(request):
    battle_data = {}
    for doc in battledata.objects.all():#すべてのデータをdocへ
        if doc.userID1 not in battle_data:
            battle_data[doc.userID1] = 0
        if doc.userID2 not in battle_data:
            battle_data[doc.userID2] = 0

    print(battle_data)
    for doc in battledata.objects.all():
        battle_data[doc.winner] +=1

    winnum = max(battle_data.values())
    Winner = [k for k, v in battle_data.items() if v == winnum]

    dic=[]
    for i in Winner:
        dic.append(i)
    print({"dic":dic})
    return render(request,'result/winner.html',{"dic":dic})

def gen_dbs(request):
    battledata.objects.all().delete()
    user = []
    for doc in Entry.objects.all():
        user.append(doc.username)
    battle_id = 1
    for i in range(len(user)):
        for j in range(i + 1, (len(user))):
            data = battledata(battleID = "game"+str(battle_id), userID1 = user[i], userID2 = user[j], winner = 'none')
            data.save()
            battle_id += 1

    battleData = battledata.objects.all()
    context = {
        'battledata' : battleData,
    }
    return render(request, 'form/syouhaikai.html',context)
    
def entry_form(request):
    plaier = PlaierForm()

    entry_text = {
        'entrytext': 'こちらからエントリーしてください',
        'plaierForm': plaier,
    }

    return render(request,'entry/entry_form.html',entry_text)


def entry_list(request):
    plaierForm = request.POST
    newentry_ID = plaierForm.get('userID')
    newentry_name = plaierForm.get('username')
    newentry_pass = plaierForm.get('password1')


    if newentry_ID == None or newentry_name == None or newentry_pass == None:
        plaier = PlaierForm()
        entry_text = {
            'entrytext': 'パスワードが入力されていません',
            'plaierForm': plaier,
        }
        return render(request, 'entry/entry_form.html', entry_text)
    else:
        pass


    for doc in Entry.objects.all():
        if doc.username == newentry_name or doc.userID == newentry_ID:
            entrylist = Entry.objects.all()
            context ={
                'msg': 'すでにエントリー済み',
                'entryinfo': entrylist,
                'count': entrylist.count,
            }
            return render(request, 'entry/entrylist.html', context)
        else:
            pass

    newentry = Entry(userID=newentry_ID,username=newentry_name,password=newentry_pass)
    newentry.save()
    plaierlist = Entry.objects.all()
    context = {
        'msg': 'エントリー完了',
        'entryinfo': plaierlist,
        'count': plaierlist.count,
    }

    return render(request, 'entry/entrylist.html', context)


def deentry_form(request):
    plaier = PlaierForm()
    deentry_text = {
        'deentrytext': '情報を入力して取り消しボタンを押してください',
        'plaierForm': plaier,
    }
    return render(request, 'entry/deentry_form.html', deentry_text)


def redeentry_form(request):
    plaier = PlaierForm()
    plaierForm = request.POST
    deentry_ID = plaierForm.get('userID')
    deentry_name = plaierForm.get('username')
    deentry_pass = plaierForm.get('password1')

    if deentry_ID == None or deentry_name == None or deentry_pass == None:

        deentry_text = {
            'deentrytext': 'パスワードが入力されていません',
            'plaierForm': plaier,
        }
        return render(request, 'etry/deentry_form.html', deentry_text)
    else:
        for doc in Entry.objects.all():
            if doc.userID == deentry_ID and doc.username == deentry_name and doc.password == deentry_pass:
                deentry = Entry.objects.get(userID = deentry_ID)
                deentry.delete()
                deentry_text = {
                    'deentrytext': 'エントリーの取り消しが完了しました',
                    'plaierForm': plaier,
                }
                return render(request, 'entry/deentry_form.html', deentry_text)
            else:
                pass

        deentry_text = {
            'deentrytext': '入力情報が間違っています',
            'plaierForm': plaier,
        }
        return render(request, 'entry/deentry_form.html', deentry_text)

def table(request):
    number3=[]
    battledatas=[]
    for doc in battledata.objects.all():
        battledatas.append({})
        battledatas[-1]["battleID"]=doc.battleID
        battledatas[-1]["userID1"]=doc.userID1
        battledatas[-1]["userID2"]=doc.userID2
        battledatas[-1]["winner"]=doc.winner
    print(battledatas)
    #battledatas.append({"battleID":"1","userID1":"miya@","userID2":"taku@","winner":"miya@"})
    #battledatas.append({"battleID":"2","userID1":"miya@","userID2":"noguchi@","winner":"none"})
    #battledatas.append({"battleID":"3","userID1":"taku@","userID2":"noguchi@","winner":"noguchi@"})
    contxt={}
    
    for doc in Entry.objects.all():
        
        
        #contxt["username"].append(doc.username)
        
        contxt[doc.username]=[]
        for doc2 in Entry.objects.all():
            
            if (doc.userID==doc2.userID):
                    contxt[doc.username].append("-")
            
            else:
                for battle in battledatas:
                    if (battle["userID1"]==doc.username and battle["userID2"]==doc2.username) or (battle["userID2"]==doc.username and battle["userID1"]==doc2.username):
                        if battle["winner"]==doc.username:
                            contxt[doc.username].append("o")
                            break
                        elif (battle["winner"]=="none"):
                            contxt[doc.username].append(" ")
                            break
                        else :
                            contxt[doc.username].append("x")
                            break
                    
        
                #contxt[doc.username].append(" ")
    print({"contxt":contxt})
    return render(request, 'table/table.html', {"contxt":contxt})