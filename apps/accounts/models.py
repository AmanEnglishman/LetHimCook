from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email

    def get_absolute_url(self):
        return reverse('profile-detail', kwargs={'pk': self.pk})
