from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('blog/', views.PostView.as_view(), name='blog'),
    path('detail/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
]
