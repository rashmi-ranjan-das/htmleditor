from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'editor/home.html')

def run(request):
    if request.method == 'POST':
        html = request.POST['html']
        print(html)
        return render(request, 'editor/home.html', {'html':html})