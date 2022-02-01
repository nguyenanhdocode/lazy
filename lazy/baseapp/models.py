from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class Grade(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class Post(models.Model):
    content = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_solved = models.BooleanField(default=False)
    is_banned = models.BooleanField(default=False)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey(Grade, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return '{}\'s post'.format(self.user.username)

    class Meta:
        ordering = ('-created', )
