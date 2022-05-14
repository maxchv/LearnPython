from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .signals import email_receive


class EmailView(View):

    def get(self, request, *args, **kwargs):
        result = email_receive.send_robust(self.__class__, email='vasja_pukin@mail.com')
        print(result)
        return redirect(reverse('demo:index'))
