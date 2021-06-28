from django.contrib import admin
#追加
from django.urls import include, path
 
urlpatterns = [
    path('admin/', admin.site.urls),
 
    #usersのURLの場合、myappのurls.pyを呼び出す
    path('users/', include('form.urls')),
]