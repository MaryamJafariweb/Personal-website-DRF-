from rest_framework.response import Response
from rest_framework.views import APIView
from .models import About
from .serializers import AboutSerializer, HomeSerializer


# Create your views here.

class HomeView(APIView):
    def get(self, request):
        info_home = About.objects.all()
        ser = HomeSerializer(instance=info_home, many=True)
        return Response(ser.data)


class AboutView(APIView):
    def get(self, request):
        info_about = About.objects.all()
        ser = AboutSerializer(instance=info_about, many=True)
        return Response(ser.data)
