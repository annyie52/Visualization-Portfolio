from django.shortcuts import render

# Create your views here.

def mainpage(request):
    return render(
        request,
        'blog/mainpage.html'
    )

def hy1(request):
    return render(
        request,
        'blog/hy1.html'
    )

def hy2(request):
    return render(
        request,
        'blog/hy2.html'
    )

def hy3(request):
    return render(
        request,
        'blog/hy3.html'
    )

def hy4(request):
    return render(
        request,
        'blog/hy4.html'
    )

def hy5(request):
    return render(
        request,
        'blog/hy5.html'
    )

def insight(request):
    return render(
        request,
        'blog/insight.html'
    )

