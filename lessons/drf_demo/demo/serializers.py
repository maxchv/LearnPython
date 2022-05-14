from rest_framework import serializers

from demo.models import Post, Comment


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    text = serializers.CharField(required=False)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance

# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ('id', 'title', 'text', 'created')
#
#
# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = ('post', 'user', 'text')
