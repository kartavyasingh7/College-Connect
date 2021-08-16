from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.loginUser, name="loginUser"),
    path('logout', views.logoutUser, name="logoutUser"),
    path('signup', views.signup, name="signup"),
    path('register', views.register, name="register"),
    path('home', views.home, name="home"),
    path('timetable', views.timetable, name="timetable"),
    path('menu', views.menu, name="menu"),
    path('paper', views.paper, name="paper"),
    url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)