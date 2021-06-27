from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PostView, CommentView, UpvoteView

router = DefaultRouter()
router.register(r"comments", CommentView)
router.register(r"posts", PostView)

urlpatterns = router.urls
urlpatterns += [path("upvote/", UpvoteView.as_view())]
