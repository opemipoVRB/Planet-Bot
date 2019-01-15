# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView, UpdateView, ListView, DetailView
from django.views.generic.detail import SingleObjectMixin

from .forms import BotForm, TenantForm, UpdateTenantForm, UpdateBotForm
# CreateBotForm
from .models import Bot, Response, Tenant, Intent


class SignUp(CreateView):
    form_class = TenantForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class IndexView(LoginRequiredMixin, View):
    login_url = '/bottieverse/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, ):
        request_user = request.user

        current_user = get_object_or_404(Tenant, user=request_user)
        print("Tenant is index ", current_user.id)
        context = {

            'current_user': current_user,
        }

        return render(request, 'planet-bot/index.html', context)


# class TenantView(View):
#
#     def get(self, request, tenant_name):
#         tenants = get_object_or_404(Tenant, name=tenant_name)
#         bots = Bot.objects.filter(tenant=tenants.id)
#         context = {"tenants": tenants,
#                    "bot_list": bots}
#
#         return render(request, 'bottieverse/tenant.html', context)
#

class TenantView(UpdateView):
    model = Tenant
    form_class = UpdateTenantForm
    template_name = 'planet-bot/profile.html'


class BotGardenView(ListView):
    template_name = 'planet-bot/bot_garden.html'

    def get_queryset(self):
        self.tenant = get_object_or_404(Tenant, pk=self.kwargs["pk"])
        self.bots = Bot.objects.filter(tenant=self.tenant.id)
        return self.bots

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the tenant
        context['tenant'] = self.tenant
        context["bot_list"] = self.bots
        return context


class BotProfileView(UpdateView):
    model = Bot
    form_class = UpdateBotForm
    template_name = 'planet-bot/bot-profile.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        self.bot = get_object_or_404(Bot, pk=self.kwargs["pk"])
        self.tenant = self.bot.tenant
        context = super().get_context_data(**kwargs)
        # Add in the tenant
        context['tenant'] = self.tenant
        context["bot"] = self.bot
        return context


# Note that you’ll need to decorate this view using login_required(), or alternatively handle unauthorized users in
# the form_valid().
class CreateBotView(CreateView):
    model = Bot
    fields = ['name', 'description']
    # form_class = BotForm
    context_object_name = "bot"
    template_name = 'planet-bot/createbot.html'

    def form_valid(self, form):
        owner = self.request.user
        self.tenant = get_object_or_404(Tenant, user=owner)
        form.instance.tenant = self.tenant
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        owner = self.request.user
        print("Check 12 12 ")
        print("Bot owner ", owner)
        self.tenant = get_object_or_404(Tenant, user=owner)
        print(self.tenant)
        self.bots = Bot.objects.filter(tenant=self.tenant.id)
        # Call the base implementation first to get a context
        context = super(CreateBotView, self).get_context_data(**kwargs)
        # Add in the tenant
        context['tenant'] = self.tenant
        context["bot_list"] = self.bots
        return context


class IntentListView(ListView):
    # paginate_by = 50
    template_name = "planet-bot/intent_list.html"

    def get_queryset(self):
        self.bot = get_object_or_404(Bot, pk=self.kwargs["pk"])
        self.intents = Intent.objects.filter(agent=self.bot.id)
        self.tenant = self.bot.tenant
        return self.intents

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bot'] = self.bot
        context['intents'] = self.intents
        context['tenant'] = self.tenant
        return context


class CreateIntentView(CreateView):
    model = Intent
    template_name = 'bottieverse/create_intents.html'


class PreviewBot(View):

    def get(self, request, **kwargs):
        bot = get_object_or_404(Bot, name=self.kwargs["bot_name"])
        bot_response = bot.description
        if bot_response:
            welcome_message = bot_response
            return render(request, 'bottieverse/bot.html',
                          {'bot': bot, 'bot_response': bot_response, 'welcome_message': welcome_message})
