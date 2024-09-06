from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/',max_length=250,null=True,default=None)
    uploaded_at = models.DateTimeField(auto_now_add=True)

