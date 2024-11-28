from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User


class AboutUser(models.Model):
    profile_picture = models.ImageField(upload_to='profile_image', blank=False, null=False)
    profile_picture_aboutme = models.ImageField(upload_to='profile_image', blank=True, null=True)
    cv_link = models.URLField(max_length=200, blank=True, null=True, unique=True)
    about_me = models.TextField(blank=True, null=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    created_by = models.ForeignKey(User, related_name='aboutuser', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class UserProject(models.Model):
    live_links_to_project = models.URLField(max_length=180, blank=True, null=True, unique=True)
    project_name = models.CharField(max_length=100, blank=False, null=False)
    about_project = models.TextField()
    project_picture = models.ImageField(upload_to='project_images', blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='userprojects', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class LinksToSocialMedia(models.Model):
    name_social_media = models.CharField(max_length=50, blank=True, null=True, unique=True)
    icon_social_media = models.ImageField(null=True, blank=True, upload_to='social_media_icons')
    links_to_social_media = models.URLField(max_length=180, blank=True, null=True, unique=True)
    created_by = models.ForeignKey(User, related_name='links', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_social_media