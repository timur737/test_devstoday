from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class UpvoteView(APIView):
    def post(self, request):
        post_id = request.data.get("post_id")
        author = request.data.get("author")
        post = get_object_or_404(Post, id=post_id)
        post.upvote(author)
        post.count_upvotes()
        post.save()
        return Response({"your_upvoted_post": post.title})
