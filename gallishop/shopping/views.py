from django.db import models
from django.db.models import fields
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from shopping.forms import SignUpForm
from shopping.models import Items

# Create your views here.
class HomeView(TemplateView):
    template_name = 'shopping/home.html'

class AddItemsView(CreateView):
    model = Items
    fields = '__all__'

class DisplayItemsView(ListView):
    model = Items

class DisplayItemListView(ListView):
    model = Items
    template_name = 'shopping/itemnames.html'

class DisplayDetailsView(DetailView):
    model = Items

class ItemsUpdateView(UpdateView):
    model = Items
    fields = '__all__'

class DeleteItemsView(DeleteView):
    model = Items
    success_url = reverse_lazy('details')

class LogoutView(TemplateView):
    template_name = 'registration/logout.html'

class SignUpView(TemplateView):
    def get(self, request):
        form = SignUpForm
        return render(request, 'shopping/signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return render(request, 'registration/signup_success.html')