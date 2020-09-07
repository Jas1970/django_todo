from django.shortcuts import render, get_object_or_404

# Create your views here.

def IndexViews(request):
    return render(request, 'todoapp/index.html')

def AboutViews(request):
    return render(request, 'todoapp/about.html')

def ContactusViews(request):
    return render(request, 'todoapp/contact.html')

def FeedbackViews(request):
    return render(request, 'todoapp/feedback.html')
