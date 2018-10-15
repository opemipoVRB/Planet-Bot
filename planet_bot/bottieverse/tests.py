from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.utils import timezone

from .models import Tenant, Bot


class TenantTestCase(TestCase):
    """This class defines the test suite for the tenant model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.tenant_name = "OneGov"
        self.tenant = Tenant(name=self.tenant_name)

    def test_model_can_create_a_tenant(self):
        """Test the bucketlist model can create a bucketlist."""
        old_count = Tenant.objects.count()
        self.tenant.save()
        new_count = Tenant.objects.count()
        self.assertNotEqual(old_count, new_count)


class BotTestCase(TestCase):
    """This class defines the test suite for the bot model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.bot_name = "Govbot"
        self.tenant_name = "OneGov"
        self.tenant = Tenant(name=self.tenant_name)
        self.tenant = Tenant.objects.get(name=self.tenant_name)
        print(" BOT ID ", self.tenant)
        self.bot = Bot(name=self.bot_name, tenant=1,  date_created= timezone.now())

    def test_model_can_create_a_bot(self):
        """Test the bot model can create a bot."""
        old_count = Bot.objects.count()
        self.bot.save()
        new_count = Bot.objects.count()
        self.assertNotEqual(old_count, new_count)
