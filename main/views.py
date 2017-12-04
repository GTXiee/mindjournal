from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.db.models.base import ObjectDoesNotExist
from django.core.exceptions import MultipleObjectsReturned
from django.forms.forms import ValidationError
from django.utils.translation import ugettext as _

@login_required()
def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            form.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('thanks')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def thanks(request):
    return render(request, 'registration/thanks.html')
