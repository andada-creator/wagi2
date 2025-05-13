#from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

class PostView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.user
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetailView(APIView):
    def put(self, request, obj_id):
        try:
            post = Post.objects.get(id=obj_id)
        except Post.DoesNotExist:
            return Response({'message': '해당 게시글이 존재하지 않습니다.'}, status=404)

        if post.user != request.user:
            return Response({'message': '권한이 없습니다.'}, status=403)

        post.content = request.data.get('content', post.content)
        post.save()
        return Response({'message': '수정 성공'})

    def delete(self, request, obj_id):
        try:
            post = Post.objects.get(id=obj_id)
        except Post.DoesNotExist:
            return Response({'message': '해당 게시글이 존재하지 않습니다.'}, status=404)

        if post.user != request.user:
            return Response({'message': '권한이 없습니다.'}, status=403)

        post.delete()
        return Response({'message': '삭제 성공'})
