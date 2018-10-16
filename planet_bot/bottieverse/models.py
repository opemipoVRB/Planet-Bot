from django.db import models


# Create your models here.


class Tenant(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    unique_identifier = models.CharField(max_length=255, blank=False, unique=True)
    secret_key = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a self.name as representation of the model instance."""
        return "{}".format(self.name)


class Bot(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a self.name as representation of the model instance."""
        return "{} belongs to {} ".format(self.name, self.tenant)


class BotResponse(models.Model):
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE)
    welcome_message = models.BooleanField(default=False)
    response = models.CharField(max_length=255, default="No message")
    required_threshold = models.FloatField(default=0.0)
    confidence_threshold = models.FloatField(default=0.0)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a self.name as representation of the model instance."""
        return "This reponse belongs to {} ".format(self.bot.name)


class ChatLog(models.Model):
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE)
    response = models.ForeignKey(BotResponse, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
