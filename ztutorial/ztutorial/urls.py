"""ztutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
#...from 파일 import 클래스
from zcomunity.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #...요청경로(정규표현식), 요청을 처리할 함수, 이름
    #...등록한 요청경로 끝에 쉼표(,)를 붙일 것.
    url(r'^write/', write, name='write'),
    #url(r'^hello/', include('zcomunity.urls')),
    url(r'^list/', list, name='list'),
    #...몇번째 페이지인지 정규표현식으로 파라미터를 받음.
    #...http://127.0.0.1:8080/view/2/ 와 같은 요청경로임.
    url(r'^view/(?P<num>[0-9]+)/$', view),
]
