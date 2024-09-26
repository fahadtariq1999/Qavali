from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "restaurant/index.html")

def test_view(request):
    return render(request, '/test.html')