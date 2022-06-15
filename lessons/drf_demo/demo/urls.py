from django.urls import path
from rest_framework.routers import DefaultRouter

from demo.views import PostViewSet, CommentViewSet

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

app_name = 'demo'

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'comments', CommentViewSet, basename='comments')
urlpatterns = [
                  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
              ] + router.urls
# from demo.views import post_list, comment_list
# from demo.views import PostList, CommentList
# urlpatterns = [
# path('api/posts', post_list),
# path('api/posts', PostList.as_view()),
# path('api/comments', comment_list),
# path('api/comments', CommentList.as_view()),
# ]
