from django.shortcuts import render
from zcomunity.zforms import *

# Create your views here.
'''
...work1.글쓰기 페이지 열기.
def write(request):
    #return HttpResponse('Hello, World. 안뇽!!')
    return render(request,'write.html')
'''

'''
...work2.모델을 이용하여 폼만들기.
def write(request):
    form = Form()
    return render(request
                  ,'write.html'
                  , {'form':form})
'''

def write(request):
    #...POST 전송방식이고 폼이 유효하면 DB 에 저장함.
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Form()

    return render(request
                  ,'write.html'
                  , {'form':form})

'''
...work3.리스트 페이지 만들기.
def list(request):
    return render(request, 'list.html')
'''

#...work4.리스트 목록 데이터 출력하기.
def list(request):
    articleList = Article.objects.all()
    return render(request, 'list.html', {'articleList':articleList})

#...work5.상세 글조회 페이지.
def view(request, num="1"):
    article = Article.objects.get(id=num)
    return render(request, 'view.html', {'article':article})

