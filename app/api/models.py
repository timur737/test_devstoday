from django.db import models


class Upvote(models.Model):
    author = models.CharField(max_length=256)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("post", "author")

    def __unicode__(self):
        return f"{self.author.name} upvoted {self.post.title}"


class Post(models.Model):
    title = models.CharField(max_length=256, unique=True)
    link = models.URLField()
    creation_date = models.DateField(auto_now_add=True)
    upvotes = models.IntegerField(null=True, default=0)
    author = models.CharField(max_length=256)

    def __unicode__(self):
        return self.title

    def count_upvotes(self):
        self.upvotes = Upvote.objects.filter(post=self).count()

    def upvote(self, author):
        Upvote.objects.get_or_create(author=author, post=self)


class Comment(models.Model):
    author = models.CharField(max_length=256)
    content = models.TextField()
    creation_date = models.DateField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey(
        "Comment",
        related_name="replies",
        on_delete=models.CASCADE,
        null=True,
        default=None,
    )

    def __unicode__(self):
        return self.content
