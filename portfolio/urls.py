from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('portfolio/', views.PortfolioView.as_view(), name='portfolio'),
    path('detail/<int:pk>/', views.PortfolioDetailView.as_view(), name='detail'),
]