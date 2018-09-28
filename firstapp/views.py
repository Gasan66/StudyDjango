from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm


def index(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data['name']
            # age = request.POST.get('age')
            return HttpResponse("<h2>Hello, {0}</h2>".format(name))
        else:
            return HttpResponse('Invalid Data')
    else:
        userform = UserForm()
        langs = ["English", "German", "French", "Spanish", "Chinese"]
        data = {"n": 0}
        return render(request, "contact.html", context={'langs': langs, 'data': data, 'form': userform})
