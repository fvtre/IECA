"""
URL configuration for IECA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup,name='signup'),
    path('tasks/', views.tasks,name='tasks'),
    path('logout/', views.signout,name='logout'),
    path('signin/', views.signin,name='signin'),
    path('create_task/', views.create_task,name='create_task'),
    path('task_detail/<int:task_id>/', views.task_detail,name='task_detail'),
    path('task_detail/<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('casadepaz/', views.casadepaz,name='casadepaz'),
    path('aviva2/', views.aviva2,name='aviva2'),
    path('avivakids/', views.avivakids,name='avivakids'),
    path('jovenes/', views.jovenes,name='jovenes'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

