from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Bot, BotResponse


def index(request):
    bots = Bot.objects.order_by('name')[:5]
    context = {
        'bot_list': bots,
    }
    return render(request, 'bottieverse/index.html', context)


def tenant_bot(request, bot_name):
    bot = get_object_or_404(Bot, name=bot_name)
    bot_response = get_object_or_404(BotResponse, bot=bot)
    return render(request, 'bottieverse/bot.html', {'bot': bot, 'bot_response': bot_response})
