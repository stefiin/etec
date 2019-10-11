from django.shortcuts import render

# Create your views here.
def index(request, page):
    return render(request, "index.html", context={"page": page})

def load_single(request):
	source_file = request.GET.get('f', 'home') + ".html"
	return render(request, source_file)