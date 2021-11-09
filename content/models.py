from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import BLANK_CHOICE_DASH



class Content(models.Model):
    content = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.content


class Cv(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    content = models.ManyToManyField(Content)
    cv = models.ForeignKey(Cv, on_delete=models.CASCADE, null=True, blank=True, related_name="section")
    def __str__(self):
        return self.name


# ////////////////////////////////////////////////////////////////////////////


class Post(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    brief_content = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.title

class PostSection(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True, related_name="post_section")

    def __str__(self):
        return self.name

class PostParagraph(models.Model):
    section = models.ForeignKey(PostSection, on_delete=models.CASCADE, null=True, blank=True, related_name="post_paragraph")
    paragraph = models.TextField()

    def __str__(self):
        return f"paragraph of section '{self.section.name}' of title '{self.section.post.title}'"

