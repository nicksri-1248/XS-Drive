from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class Home(LoginRequiredMixin, TemplateView):
  context_object_name = 'posts'
  template_name = 'main/home.html'
  login_url = 'auth/login'