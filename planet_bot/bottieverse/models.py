from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.crypto import get_random_string


# Create your models here.


class Tenant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False, unique=True)
    unique_identifier = models.CharField(max_length=255, blank=False, unique=True)
    secret_key = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a self.name as representation of the model instance."""
        return "{}".format(self.user.email)

    def get_absolute_url(self):
        return reverse('tenant', kwargs={'pk': self.pk})

    # def _generate_unique_identifier(self):
    #     unique_identifier = get_random_string(length=32, allowed_chars='0123456789')
    #     return unique_identifier
    #
    # def _secret_key_(self):
    #     secret_key = get_random_string(length=32, allowed_chars='abcdefghijklmnopqrstuvwxyz'
    #                                                             'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#$%*@()!?')
    #     return secret_key
    #
    # def save(self, *args, **kwargs):
    #     if not self.unique_identifier:
    #         self.unique_identifier = self._generate_unique_identifier()
    #         self.secret_key = self._secret_key_()
    #     super().save(*args, **kwargs)

    @receiver(post_save, sender=User)
    def create_tenant(sender, instance, created, **kwargs):
        if created:
            Tenant.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_tenant(sender, instance, **kwargs):
        instance.tenant.save()


class Bot(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='bots')
    name = models.CharField(max_length=255, blank=False, unique=True)
    description = models.CharField(max_length=255, blank=False, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a self.name as representation of the model instance."""
        return "{} belongs to {} ".format(self.name, self.tenant)

    def get_absolute_url(self):
        return reverse('bot_profile', kwargs={'pk': self.pk})


class Intent(models.Model):
    agent = models.ForeignKey(Bot, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=255, )

    # context = ""
    # events = ""
    # fulfilement=""

    def __str__(self):
        """Return a self.name as representation of the model instance."""
        return "Intent {} belongs to {} ".format(self.intent, self.tenant)


class TrainingPhrase(models.Model):
    intent = models.ForeignKey(Intent, on_delete=models.CASCADE, related_name="training_phrase")
    phrase = models.CharField(max_length=255, blank=False, unique=False)

    def __str__(self):
        """Return a self.name as representation of the model instance."""
        return self.phrase


class Parameter(models.Model):
    required = models.BooleanField()
    name = models.CharField(max_length=255, )
    entities = models.ForeignKey(Bot, on_delete=models.CASCADE)
    value = models.CharField(max_length=255, )

    # list= models.BooleanField()

    def __str__(self):
        """Return a self.name as representation of the model instance."""
        return self.name


class Action(models.Model):
    intent = models.OneToOneField(Intent, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, )
    parameters = models.ManyToManyField(Parameter)

    def __str__(self):
        """Return a self.name as representation of the model instance."""
        return self.name


class Response(models.Model):
    intent = models.ForeignKey(Intent, on_delete=models.CASCADE, related_name="response")
    response = models.CharField(max_length=255)

    def __str__(self):
        """
        Return a self.name as representation of the model instance.
        """
        return self.name


class ChatLog(models.Model):
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE, related_name='chat_logs')
    response = models.ForeignKey(Response, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
