
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.http import HttpResponse

def setcookie(request):
    response = HttpResponse("Python tutorial")
    response.set_cookie('user_id', '23')

    return response


def getcookie(request):
    cookie = request.COOKIES['user_id']
    return HttpResponse(cookie)


def setsession(request):
    request.session['sname'] = 'irfan'
    request.session['semail'] = 'irfan.sssit@gmail.com'
    return HttpResponse("session is set")

def getsession(request):
    studentname = request.session['sname']
    studentemail = request.session['semail']
    return HttpResponse(studentname+" "+studentemail)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('cookie-get/', setcookie), 
    path('cookie-set/', getcookie),

    path('session-get/', getsession), 
    path('session-set/', setsession),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
