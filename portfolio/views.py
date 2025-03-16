from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Portfolio
from .serializers import PortfolioSerializer, PortfolioDetailSerializer


# Create your views here.

class PortfolioView(APIView):
    def get(self, request):
        list_portfolio = Portfolio.objects.all()
        ser = PortfolioSerializer(instance=list_portfolio, many=True)
        return Response(ser.data)


class PortfolioDetailView(APIView):
    def get(self, request, pk):
        detail = Portfolio.objects.get(id=pk)
        ser = PortfolioDetailSerializer(instance=detail)
        return Response(ser.data)

