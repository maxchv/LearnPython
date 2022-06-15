from django.shortcuts import render
from rest_framework import status, viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from api.serializers import PostSerializer
from demo.models import Post


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    #permission_classes = [permissions.IsAuthenticated]

# @api_view(['GET', 'POST'])
# def post_list(request):
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request.data)
#         serializer = PostSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET'])
# def post_get(request, pk=None):
#     if request.method == 'GET':
#         try:
#             post = Post.objects.get(pk=pk)
#             serializer = PostSerializer(post)
#             return Response(serializer.data)
#         except:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#     return Response(status=status.HTTP_400_BAD_REQUEST)
