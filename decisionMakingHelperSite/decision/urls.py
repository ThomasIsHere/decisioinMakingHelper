from django.urls import path

from . import views

app_name = 'decision'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #path('', views.saveQuestionInDB, name='saveQuestionInDB'),
]
