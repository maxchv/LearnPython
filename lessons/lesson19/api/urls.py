from django.urls import path

# from api.views import post_list, post_get
from rest_framework import routers

from api.views import PostViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
# router.register('comments', CommentViewSet)

urlpatterns = router.urls

# urlpatterns = [
#     path('posts/', post_list),
#     path('posts/<int:pk>/', post_get),
# ]