from rest_framework import serializers
from posts.models import Post as PostModel

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model=PostModel
        fields=["content","user"]