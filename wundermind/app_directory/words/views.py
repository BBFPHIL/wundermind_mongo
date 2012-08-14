from django.views.generic import FormView, TemplateView, ListView, DetailView, UpdateView, RedirectView, UpdateView
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class IndexView(TemplateView):
    """
    This view only show a template for now
    """
    template_name = "index.html"
