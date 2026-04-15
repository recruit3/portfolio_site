from django.shortcuts import render

def index(request):
    return render(request, 'portfolio/index.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def ai_board(request):
    return render(request, 'portfolio/ai_board.html')

def ai_chat(request):
    return render(request, 'portfolio/ai_chat.html')

def mysite(request):
    return render(request, 'portfolio/mysite.html')