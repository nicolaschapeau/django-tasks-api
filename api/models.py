from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings



def user_directory_path(instance, filename):
    """
    Will return the folder where the image should be saved (corresponding to user id).
    """
    return f'user_{instance.user.id}/{filename}'

def task_directory_path(instance, filename):
    """
    Will return the folder where the image should be saved (corresponding to owner id).
    """
    return f'user_{instance.owner.id}/tasks/{filename}'


class User(AbstractUser):
    """
    User used for authentification
    """
    # Override default username field to make it optional
    username = models.CharField(blank=True, null=True, max_length=64, unique=False)
    # Override default email field with unique=True
    email = models.EmailField(_("Email address"), unique=True)

    # Set authentification field to email
    USERNAME_FIELD = 'email'
    # Required fields for superusers
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return f'{self.email}'


class UserProfile(models.Model):
    """
    User profile, with all the fields needed. One to one relationship with User.
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(_("Profile picture"), upload_to=user_directory_path, height_field=None, width_field=None, max_length=None, blank=True)
    profile_banner = models.ImageField(_("Profile banner"), upload_to=user_directory_path, height_field=None, width_field=None, max_length=None, blank=True)

    class Meta:
        """
        User Profile options.
        """
        verbose_name_plural = "User Profile"




class Task(models.Model):
    """
    Task model, with all the fields needed.
    """
    owner = models.ForeignKey("api.User", related_name="tasks", on_delete=models.CASCADE)
    title = models.CharField(_("Task title"), max_length=100)
    description = models.TextField(_("Task description"), max_length=500)
    completed = models.BooleanField(_("Task status"), default=False)
    task_picture = models.ImageField(_("Task picture"), upload_to=task_directory_path, height_field=None, width_field=None, max_length=None)

    # Model Options
    # class Meta:
    #     """
    #     Snipet meta class for Model options.
    #     """
    #     ordering = ['created']
