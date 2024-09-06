from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/',max_length=250,null=True,default=None)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Topic(models.Model):
    topic_name = models.CharField(max_length=255)
    topic_doc = models.CharField(max_length=255)
    topic_time = models.CharField(max_length=10)

    def __str__(self):
        return self.topic_name

class Chapter(models.Model):
    name = models.CharField(max_length=255)
    topics = models.ManyToManyField(Topic, related_name='chapters')

    def __str__(self):
        return self.name