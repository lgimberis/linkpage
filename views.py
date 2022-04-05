from django.shortcuts import render

from .models import Link
def links(request):
    context = {
        "links": Link.objects.all()
    }
    return render(request, "links.html", context=context)