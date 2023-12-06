from django.shortcuts import render

# Create your views here.
def index(request):
    """Main page Gao Bay"""
    return render(request, 'webapp/index.html')