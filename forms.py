from django.forms import ModelForm

from .models import Link

class LinkForm(ModelForm):
    model = Link