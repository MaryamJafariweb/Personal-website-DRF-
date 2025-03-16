from rest_framework import serializers
from .models import EducationExperiences, Skills


class EducationExperiencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationExperiences
        fields = '__all__'


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'
