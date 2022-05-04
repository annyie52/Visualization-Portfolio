from django.shortcuts import render

# Create your views here.
def home(request):
    return render(
        request,
        'single_pages/home.html'
    )

def purpose(request):
    return render(
        request,
        'single_pages/purpose.html'
    )

def review(request):
    return render(
        request,
        'single_pages/review.html'
    )