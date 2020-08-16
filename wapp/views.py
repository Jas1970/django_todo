from django.shortcuts import render

# Create your views here.

def IndexViews(request):
    return render(request, 'wapp/index.html')

def AboutViews(request):
    return render(request, 'wapp/about.html')

def ContactusViews(request):
    return render(request, 'wapp/contact.html')

def FeedbackViews(request):
    return render(request, 'wapp/feedback.html')
