from django.urls import path
from . import views
from .views import text_detail, index, text_detail, hsk_texts

urlpatterns = [
    path("", views.index, name="index"),
    path("excercises/", views.excercises, name="excercises"),
    path('text/<int:text_id>/', text_detail, name='text_detail'),
    path('hsk/<int:hsk_level>/', hsk_texts, name='hsk_texts'),  
    path('paragraph_blankedeasy/<int:text_id>/<int:p_number>/', views.paragraph_blankedeasy, name='paragraph_blankedeasy'),
]
