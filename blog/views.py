from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


# Create your views here.

class PostView(APIView):
    def get(self, request):
        post = Post.objects.all()
        ser = PostSerializer(instance=post, many=True)
        return Response(ser.data)


class PostDetailView(APIView):
    def get(self, request, pk):
        detail = Post.objects.get(id=pk)
        ser = PostSerializer(instance=detail)
        return Response(ser.data)

    def post(self, request, pk):
        comments = Comment.objects.get(id=pk)
        ser = CommentSerializer(data=request.data, context={'request': request}, instance=comments)
        if ser.is_valid():
            ser.save()
            return Response({'response': 'Done'})
        return Response(ser.errors)
