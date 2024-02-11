from django.urls import path, include 
from . import views 

app_name = 'enquete'
urlpatterns = [
    path('',views.index, name='index'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
