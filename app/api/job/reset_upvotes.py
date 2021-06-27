from app.api.models import Post

def reset_upvotes():
    Post.upvotes.through.objects.all().delete()


if __name__ == '__main__':
    reset_upvotes()
