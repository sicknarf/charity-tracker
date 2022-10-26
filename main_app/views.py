from re import template
from django.shortcuts import render
from django import forms
from django.forms import ModelForm
import boto3
import uuid

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Donation, DONOS
from .forms import NewDonoForm
from main_app import forms
# Create your views here.

def home(request):
    return render(request, "home.html")

@login_required
def dono_index(request):
    donations = Donation.objects.filter(completed=False).order_by('-created_time')
    completed = Donation.objects.filter(completed=True).order_by('-created_time')
    return render(request, 'donations/index.html', {'donations':donations, 'completed':completed})

class NewDono(LoginRequiredMixin, CreateView):
    model = Donation
    fields = ['amount', 'donator', 'pokemon' ]

    def form_valid(self, form):
        if form.instance.amount == int(50):
            form.instance.blindfolded = True
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse('index')

class DonoDelete(DeleteView):
    model=Donation
    success_url = '/donos'

def dono_complete(request, dono_id):
    completed = Donation.objects.get(id=dono_id)
    completed.completed = True
    completed.save()
    return redirect('/donos')

def dono_uncomplete(request, dono_id):
    completed = Donation.objects.get(id=dono_id)
    completed.completed = False
    completed.save()
    return redirect('/donos')