from django.shortcuts import render
from common.models import Digimon
from django.views.generic import( 
                                    TemplateView,
                                    View,ListView,
                                    DetailView,UpdateView
                                )
from django.http import JsonResponse
from django.shortcuts import reverse
from django.contrib.messages.views import SuccessMessageMixin
from .models import Digimon
from .forms import UpdateDigimonForm
import json


class DigimonListView(TemplateView):
    template_name="digimon_list.html"


class AddToFavView(View):
    def post(self,request,*args, **kwargs):
        response={}
        data=json.loads(request.POST.get('digimon_object'))
        data["is_favorite"]=True
        digimon=Digimon(**data)
        digimon.save()
        # success_url="/"
        response["message"]="successfully added to favorite"
        response["status_code"]="200"
        return JsonResponse(response,safe=False)
        

class FavoriteDigimonListView(ListView):
    model=Digimon
    context_object_name="digimon_list"
    template_name="digimon_fav_list.html"


class DigimonDetailView(SuccessMessageMixin,UpdateView,DetailView):
    model=Digimon
    template_name="digimon_detail.html"
    context_object_name="digimon"
    form_class=UpdateDigimonForm
    success_message="Digimon updated successfully"


class DeleteDigimonView(View):
    def post(self,request,*args, **kwargs):
        response={}
        digimon=request.POST.get("pk")
        digimon=Digimon.objects.get(pk=int(digimon))
        digimon.delete()
        response["message"]="deleted successfully"
        response["url_redirect"]=reverse("digimon_fav_list")
        return JsonResponse(response,safe=False)