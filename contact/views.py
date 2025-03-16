from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Contact
from .serializers import ContactSerializer


# Create your views here.

class ContactView(APIView):
    def get(self, request):
        contact = Contact.objects.all()
        ser = ContactSerializer(instance=contact, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = ContactSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

