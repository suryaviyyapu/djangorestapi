from forum.models import ForumArticle
from rest_framework import viewsets, permissions
from .serializers import ForumSerializer

class ForumArticleViewSet(viewsets.ModelViewSet):
    queryset = ForumArticle.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ForumSerializer
