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
]