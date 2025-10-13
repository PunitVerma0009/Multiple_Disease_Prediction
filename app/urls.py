from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.index,name='index'),
    path('diabetes.html', views.diabetes,name='diabetes'),
    path('brain.html', views.brain,name='brain'),
    path('lungs.html', views.lungs,name='lungs'),
    path('kidney.html', views.kidney,name='kidney'),
    path('heart.html', views.heart,name='heart'),
    path('liver.html', views.liver,name='liver'),
    path('dia_predict', views.dia_predict,name='dia_predict'),
    path('liver_predict', views.liver_predict,name='liver_predict'),
    path('heart_predict', views.heart_predict,name='heart_predict'),
    path('brain_predict', views.brain_predict,name='brain_predict'),
    path('lungs_predict', views.lungs_predict,name='lungs_predict'),
    path('kidney_predict', views.kidney_predict,name='kidney_predict'),
]