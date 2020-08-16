from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.IndexViews , name= 'IndexViews'),
    path('about', views.AboutViews, name= 'AboutViews'),
    path('feedback', views.FeedbackViews, name= 'FeedbackViews'),
    path('contactus', views.ContactusViews, name= 'ContactusViews'),
]
