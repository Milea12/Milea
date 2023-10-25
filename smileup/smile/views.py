from django.http import HttpResponse
from django.template import loader

def smile(request):
  template = loader.get_template('Milea.html')
  return HttpResponse(template.render())