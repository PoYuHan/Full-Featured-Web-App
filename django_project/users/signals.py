from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# Want user profile to be created for each user


@receiver(post_save, sender = User) # when user is saved, send the save signal, the save signal will be receive by the receiver
def create_profile(sender, instance, created, **kwargs): # and the receiver is this create_profile function, this create_profile
    if created:                                          # takes all of the args that post_save signal pass to it
        Profile.objects.create(user = instance)


@receiver(post_save, sender = User) 
def save_profile(sender, instance, **kwargs):
    instance.profile.save()