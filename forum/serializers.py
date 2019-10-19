from rest_framework import serializers
from forum.models import ForumArticle
class ForumSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ForumArticle
        fields = '__all__'
