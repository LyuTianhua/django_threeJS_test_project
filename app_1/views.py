from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'name': 'LyuTianhua'}
    return render(request, 'home.html', context)

def threeJS(request):
    return render(request, 'threeJS.html')
