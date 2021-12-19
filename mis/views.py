from django.shortcuts import render

# Create your views here.
def mis_index(request):
    return render(request, "mis/index.html")
