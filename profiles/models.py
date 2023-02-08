from django.db import models

# Create your models here.
class UserProfile(models.Model):
    # upload_to will dive into a root directory to find a file, if not defined 
    # in settings.py (MEDIA_ROOT = BASE_DIR / "uploads”)
    # image = models.FileField(upload_to="images")

    # You can also use ImageField (so it will only accept images)

    image = models.ImageField(upload_to="images")
    