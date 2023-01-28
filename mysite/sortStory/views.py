from django.shortcuts import render

# Create your views here.
def index(request):
  temp_name = 'sortStory/index.html'
  context = {
    'title':'Neuromancer'
  }
  return render(request, temp_name, context)
  