from django.urls import path
from . import views

urlpatterns = [
    path('learndj/', views.learn_django),
    path('learndt/', views.know_date_time),
    path('learnvf/', views.value_format),
    path('learncon/', views.learn_condition),
]
