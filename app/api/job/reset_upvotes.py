from app.api.models import Upvote

def reset_upvotes():
    Upvote.objects.all().delete()


if __name__ == '__main__':
    reset_upvotes()
