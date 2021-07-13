from django.views.generic import ListView ,TemplateView,DetailView
from .models import Snack

class Index(TemplateView):
  template_name='index.html'

class SnackListView(ListView):
  template_name='snacks_list.html'
  model=Snack  

class SnackDetailView(DetailView):
  template_name='snack_details.html'
  model=Snack  
# Create your views here.
