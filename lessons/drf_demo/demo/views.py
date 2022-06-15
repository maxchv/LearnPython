from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from demo.models import Post, Comment
from demo.serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated


# @api_view(['GET', 'POST'])
# def post_list(request, format=None):
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = PostSerializer(data=data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class PostList(APIView):
#     def get(self, request, format=None):
#         snippets = Post.objects.all()
#         serializer = PostSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class PostList(ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)


# @api_view(['GET', 'POST'])
# def comment_list(request, format=None):
#     if request.method == 'GET':
#         comments = Comment.objects.all()
#         serializer = CommentSerializer(comments, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = CommentSerializer(data=data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CommentList(APIView):
#     def get(self, request, format=None):
#         snippets = Comment.objects.all()
#         serializer = CommentSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = CommentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class CommentList(ListCreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)
