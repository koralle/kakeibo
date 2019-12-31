from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View
from .models import Balance
from . forms import BalanceForm
from django.urls import reverse_lazy
import logging
from django.conf import settings
import os

# Create your views here.
def index_func(request):
  return render(request, 'base.html')


class BalanceList(ListView):
  context_object_name = 'balance'
  template_name = 'balance_list.html'
  model = Balance

class DetailBalance(DetailView):
  context_object_name = 'balance'
  template_name = 'balance_detail.html'
  model = Balance

def balance_edit(request, balance_id=None):

  if balance_id:
    balance = get_object_or_404(Balance, pk=balance_id)
  else:
    balance = Balance()
  
  if request.method == 'POST':
    form = BalanceForm(request.POST, instance=balance)
    if form.is_valid():
      balance = form.save()
      return redirect('app:balance_list')
  else:
    form = BalanceForm(instance = balance)

  return render(request, 'balance_edit.html', dict(form=form, balance_id=balance_id))

class FrontedAppView(View):

  def get(self, request):
    try:
      with open(os.path.join(settings.REACT_APP_DIR), 'build', 'index.html') as f:
        return HttpResponse(f.read())
    except FileNotFoundError:
      logging.exception('Production build of app not found')
      return HttpResponse(
        """
        This URL is only used when you have built the production
        version of the app. Visit http://localhost:3000/ instead, or
        run `yarn run build` to test the production version.         
        """,
        status = 501
      )