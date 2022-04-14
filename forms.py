from django.forms import ModelForm

from .models import Link

class LinkForm(ModelForm):
    class Meta:
        model = Link
        fields = ["name", "link_url", "description"]