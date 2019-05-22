"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def index(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'메인 페이지',
            'year':datetime.now().year,
        }
    )

def loginPage(request):
    return render(request,'app/login.html')

def result(request):
    assert isinstance(request, HttpRequest)
    # 데이터를 받음
    search_keyword = request.POST.get('search_keyword')

    return render(
        request,
        'app/result.html',
        {
            'title': search_keyword + '매출 데이터 분석결과',
            'search_keyword': search_keyword,
            'year':datetime.now().year,
        }
    )

def result_tweet(request):
    assert isinstance(request, HttpRequest)
    # 데이터를 받음

    return render(
        request,
        'app/result_tweet.html',
        {
            'year':datetime.now().year,
        }
    )

def result_youtube(request):
    assert isinstance(request, HttpRequest)
    # 데이터를 받음

    return render(
        request,
        'app/result_youtube.html',
        {
            'year':datetime.now().year,
        }
    )