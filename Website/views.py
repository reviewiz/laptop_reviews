from django.shortcuts import render

# Create your views here.
class authentication:
    def login(request):
        context={'data':'hi'}
        return render(request, 'authentication/login.html',context)