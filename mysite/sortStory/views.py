from django.shortcuts import render

from .models import sortstory, storytheme

# Create your views here.
def index(request):
  temp_name = 'sortStory/index.html'
  context = {
    'story_list': sortstory.objects.all(),
    'story_theme': storytheme.objects.all(),
  }
  return render(request, temp_name, context)
  