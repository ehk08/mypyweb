from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from board.models import Question
from board.forms import QuestionForm, AnswerForm


def index(request):
    return render(request, 'board/index.html')
    # return HttpResponse("<h1>웹 메인 페이지 입니다.</h1>")

def question_list(request):
    question_list = Question.objects.all()
    context = {'question_list': question_list}
    return render(request, 'board/question_list.html', context)

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'board/detail.html', context)

# 질문 등록
@login_required(login_url='common:login')
def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST) #입력된 데이터가 있는 폼
        if form.is_valid(): # 폼이 유효성 검사를 통과했다면
            question = form.save(commit=False)  #가저장
            question.create_date = timezone.now()  # 등록일 생성
            form.save() #실제 저장
            return redirect('board:question_list') # 질문 목록 페이지 이동
    else: #get 방식
        form = QuestionForm()    #폼 객체 생성(빈 폼 생성)
    context = {'form': form}
    return render(request, 'board/question_form.html', context)

# 답변 등록
@login_required(login_url='common:login')
def answer_create(request, question_id):
    # 질문이 1개 있어야 답변을 등록할 수 있음
    question = Question.objects.get(id=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False) #content만 저장
            answer.create_date = timezone.now() #답변 등록일
            answer.question = question  #외래키 생성
            form.save()
            return redirect('board:detail', question_id=question.id) #question.id 주의!!
    else:
        form = AnswerForm()   #빈 폼 생성
    context = {'question': question, 'form': form}
    return render(request, 'board/detail.html', context)