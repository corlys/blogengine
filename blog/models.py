from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils.text import slugify

from time import time

# Create your models here.

STATUS = ((0, "Draft"), (1, "Publish"))


class Post(models.Model):
    title = models.CharField(unique=True, max_length=200)
    slug = models.SlugField(unique=True, max_length=200, blank=True)
    # author harus pakai null=True, kalau ngga pas pakai commit = False di forms nya bakal ngilangin tags nya (?)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts", null=True
    )
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    tags = models.ManyToManyField("Tag", blank=True, related_name="posts")

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

    def get_update_url(self):
        return reverse("post_update", kwargs={"slug": self.slug})

    def get_delete_url(self):
        return reverse("post_delete", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)


class Tag(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tags_detail", kwargs={"slug": self.slug})

    def get_update_url(self):
        return reverse("tags_update", kwargs={"slug": self.slug})

    def get_delete_url(self):
        return reverse("tags_delete", kwargs={"slug": self.slug})


def gen_slug(s):
    slug = slugify(s, allow_unicode=True)
    return slug + f"-{int(time())}"

