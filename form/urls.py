from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.showUsers, name='showUsers'),
    path('<str:user>', views.showDetail, name='showDetail'),
    path('create/', views.showCreateUserForm, name='showCreateUserForm'),
    path('add/',views.addUsers,name='addUser'),
    path('<str:user>/update/', views.updateUser, name='updateUser'),
    path('<str:user>/edit/', views.showEditUserForm, name='showEditUserForm'),
    path('syouhai/',views.syouhaiForm,name='syouhai'),
    path('<str:Id>/win/',views.syouriData,name='syouriData'),
    path('winner/',views.win,name='winner'),
    path('generate/',views.gen_dbs,name='generate'),
    path('entry/', views.entry_form, name='entry_form'),
    path('entrylist/', views.entry_list, name='entry_list'),
    path('deentry/', views.deentry_form, name='deentry_form'),
    path('redeentry/', views.redeentry_form, name='redeentry_form'),
    path('table/', views.table, name='table'),
]