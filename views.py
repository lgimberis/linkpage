from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ValidationError

import json, ast

from .models import Link
from .forms import LinkForm

def links(request):
    if request.method == "POST":
        form = LinkForm(request.POST)
    else:
        form = LinkForm()
    context = {
        "links": [{"ID": link.id, "Name": link.name, "URL": link.link_url, "Description": link.description} for link in Link.objects.all()],
        "link_form": form,
    }
    return render(request, "linkpage/links.html", context=context)

def link_search(request):
    if request.method == "GET":
        search_text = request.GET["link-search"]
        return JsonResponse({'links': list(Link.objects.filter(name__icontains=search_text))})

def link_create(request):
    data = json.loads(request.body.decode('utf-8'))
    link_name = data["Name"]
    link_url = data["URL"]
    link_description = data["Description"]

    try:
        link = Link(name=link_name, link_url=link_url, description=link_description)
        link.clean()
        link.save()
        return JsonResponse({"code": 200, "message": "", "created_id": link.id})
    except ValidationError as e:
        print(e)
        return JsonResponse({"code": 400, "message": str(e)})
