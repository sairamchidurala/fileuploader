# from django.db import models

# class UploadedFile(models.Model):
#     file_name = models.CharField(max_length=255)
#     public_id = models.CharField(max_length=255, default='dummy')
#     cloudinary_url = models.URLField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.file_name

from django.db import models
from django.utils import timezone

class UploadedFile(models.Model):
    file_name = models.CharField(max_length=255)
    public_id = models.CharField(max_length=255, default='dummy')
    cloudinary_url = models.URLField()
    secure_url = models.URLField(blank=True)  # Store secure URL separately
    file_type = models.CharField(max_length=50, blank=True)
    file_size = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.file_name} (ID: {self.public_id})"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Uploaded File'
        verbose_name_plural = 'Uploaded Files'
