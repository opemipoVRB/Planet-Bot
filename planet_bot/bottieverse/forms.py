#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$...........................................................................$$
$$..........................$$$$$$$$$$$$$....................................$$
$$.......................$$$$$$$$$$$$$$$$$$$.................................$$
$$.....................$$$$$$$$$$$$$$$$$$$$$$$...............................$$
$$....................$$$$$$$$$$$$$$$$$$$$$$$$$..............................$$
$$...................$$$$$$$$$$$$$$$$$$$$$$.$$...............................$$
$$...................$$$$$$$$$$$$$$$$$$$$$...$$..............................$$
$$...................$$$$$$$$$$$$$$$$$$.$$...$$$.............................$$
$$...................$$$$$$$$$$$$$$$$$$$$$$$$$$..............................$$
$$....................$$$$$$$$$$$$$.....$$$$$$$$$............................$$
$$......................$$$$$$$$$$$$$$$$..$$$$$$$............................$$
$$...................................$$$.....................................$$
$$.................$$................$$$$ $$$$$$$........$...................$$
$$...............$$$$$$..............$$$$$$$$$$$$$...$$$$$$..................$$
$$............$$$$..$$$$$.........................$$$$$$$$$..................$$
$$............$$$$...$$$$$$$....................$$$$$$.$$.$$.................$$
$$...............$$$$$$$$$$$$$$............$$$$$$$$..........................$$
$$.........................$$$$$$$$$...$$$$$$$...............................$$
$$..............................$$$$$$$$$$...................................$$
$$..........................$$$$$....$$$$$$$$$...............................$$
$$............$$.$$$$$$$$$$$$$............$$$$$$$$$$$$$$$$$..................$$
$$............$$.$$..$$$$.....................$$$$$$$$$$$$$$.................$$
$$..............$$$$$$............................$$.$$$$$$$.................$$
$$..................                                   ......................$$
$$.................. @@@  @@@  @@@@@@@        @@@@@@@ .......................$$
$$.................. @@@  @@@  @@@   @@@@     @@@   @@@@.....................$$
$$.................. @@!  @@@  @@!   !@@      @@!   !@@......................$$
$$.................. !@!  @!@  !@!   !@!      !@!   !@!......................$$
$$.................. @!@  !@!  !!@!@!!@@!     !!@!@!!@@!.....................$$
$$.................. !@!  !!!  !!!      !!!   !!!     !!!....................$$
$$.................. :!:  !!:  !!:      :!!   !!:     :::....................$$
$$................... ::!!:!   :!:      :!:   :!:     :::....................$$
$$.................... ::::    :::      :::   :::     :::....................$$
$$...................... :      :        :      :::::::  ....................$$
$$...........................................................................$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$***************************************************************************$$
$$      forms.py  Created by  Durodola Opemipo 2018                          $$
$$            Personal Email : <opemipodurodola@gmail.com>                   $$
$$                 Telephone Number: +2348182104309                          $$
$$***************************************************************************$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                                                                                           
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Tenant, Bot
from django.forms import inlineformset_factory


class TenantForm(UserCreationForm):
    name = forms.CharField(label="Tenant name/Company name/Organisation name")
    unique_identifier = forms.CharField(label="Tenant ID", help_text=" Enter any value you would "
                                                                     "like you application or device to use in "
                                                                     "communicating with your account. This would be "
                                                                     "your unique identifier")
    secret_key = forms.EmailField(label="Tenant  Key", help_text=" Enter any value you would "
                                                                 "like you application or device to use in "
                                                                 "communicating with your account This would be your "
                                                                 "application or device "
                                                                 "passkey and you can always change it ")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',
                  'name', 'unique_identifier', 'secret_key')

    def __init__(self, *args, **kwargs):
        super(TenantForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {'class': 'input100'}


class BotForm(forms.ModelForm):
    owner = forms.IntegerField(widget=forms.HiddenInput())
    name = forms.CharField(label='Bot name',
                           max_length=100,
                           widget=forms.TextInput(
                               attrs={"name": "bot_name", "id": "bot_name", "placeholder": "Nicholas"})
                           )
    description = forms.CharField(label='Description',
                                  max_length=255,
                                  widget=forms.TextInput(
                                      attrs={"name": "bot_description", "id": "bot_description", "placeholder": "I\'m "
                                                                                                                "a "
                                                                                                                "great cook"})
                                  )

    class Meta:
        model = Bot
        fields = ("name", "owner", "description")


class UpdateBotForm(forms.ModelForm):
    class Meta:
        model = Bot
        fields = ("name", "description")


# class CreateBotForm(forms.ModelForm):
#     class Meta:
#         model = Bot
#         fields = ("name", "owner")
#

class UpdateTenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ('name', 'unique_identifier', 'secret_key',)
