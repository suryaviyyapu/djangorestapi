from rest_framework import routers
from .api import ForumArticleViewSet

router = routers.DefaultRouter()
router.register('api/forum', ForumArticleViewSet, 'forum')

urlpatterns = router.urls
