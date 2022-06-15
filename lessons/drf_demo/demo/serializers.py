from rest_framework import serializers

from demo.models import Post, Comment


#
# class CommentSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     text = serializers.CharField(required=True)
#     created = serializers.DateTimeField(required=False)
#     post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
#
#     def create(self, validated_data):
#         return Comment.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.text = validated_data.get('text', instance.text)
#         instance.post = validated_data.get('post', instance.post)
#         instance.save()
#         return instance
#
#
# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=100)
#     text = serializers.CharField(required=False)
#     comments = CommentSerializer(many=True, read_only=True)
#     created = serializers.DateTimeField(required=False)
#
#     def create(self, validated_data):
#         return Post.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.text = validated_data.get('text', instance.text)
#         instance.save()
#         return instance

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'comments', 'created')
        depth = 1


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text', 'post', 'created')
