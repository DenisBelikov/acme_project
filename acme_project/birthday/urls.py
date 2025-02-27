# birthday/urls.py
from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'birthday'

urlpatterns = [
    path('create/', login_required(views.BirthdayCreateView.as_view()), name='create'),
    path('login_only/', views.simple_view),
    path('list/', views.BirthdayListView.as_view(), name='list'),
    path('<int:pk>/', views.BirthdayDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.BirthdayUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.BirthdayDeleteView.as_view(), name='delete'),
    path('', views.HomePage.as_view(), name='homepage'),
]
