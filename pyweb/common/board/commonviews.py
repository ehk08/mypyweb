from django.shortcuts import redirect
from django.utils import timezone

from common.board.commonforms import UserForm
from common.board.models import Question


# 회원 가입
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save() #화원 가입 db에 저장
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authentidcate(username=username, password=password)
            login(request, user)    #자동 로그인
            return redirect('/')    #index 페이지로 이동
        else:
            form = UserForm()   #반품 생성
        context = {'form'}
        if form.is_valid():
            question = form.save(commit=False) #가저장
            question.author = request.user #세션 권한(로그인한) 있는 글쓴이
            question.create_date = timezone.now() # 등록일 생성
            form.save() #실제 저장
            return redirect('board:question_list') # 질문 목록 페이지 이동
        else: #get 방식
            form = Question.create_date = timezone.now() # 등록일 생성
            form.save()  #실제 저장
            return redirect('board:question_list')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = autnenticate(username=username, password=password)
            login(request, user)    #자동 로그인
            return redirect('/')    #index 페이지로 이동
    else:
        form = UserForm()   #반품 생성
    context = {'form': form}

