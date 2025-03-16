from rest_framework.response import Response
from rest_framework.views import APIView
from .models import EducationExperiences, Skills
from .serializers import EducationExperiencesSerializer, SkillsSerializer


# Create your views here.

class EducationView(APIView):
    def get(self, request):
        ex = EducationExperiences.objects.all()
        ser_ex = EducationExperiencesSerializer(instance=ex, many=True)
        return Response(ser_ex.data)


class SkillsView(APIView):
    def get(self, request):
        sk = Skills.objects.all()
        ser_sk = SkillsSerializer(instance=sk, many=True)
        return Response(ser_sk.data)


