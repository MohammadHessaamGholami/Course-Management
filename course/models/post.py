from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    subject = models.CharField(max_length=100)
    text = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    attachment = models.FileField(upload_to="course/posts/assignments")
    course = models.ForeignKey("course.Course", on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "Post"

    def __str__(self):
        return self.subject


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=2000)

    class Meta:
        db_table = "PostComment"

    def __str__(self):
        return "post: " + str(self.post) + ", comment: " + str(self.id)
