from django.urls import path
from . import views

app_name = 'resume'
urlpatterns = [
    path('education/', views.EducationView.as_view(), name='education'),
    path('skills/', views.SkillsView.as_view(), name='skills'),
]
