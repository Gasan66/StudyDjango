from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .forms import UserForm
from .models import Person
from .models import Company
from django.db.models import F


# получение данных из бд
def index(request):

    companies = Company.objects.all()
    return render(request, 'index.html', {'companies': companies})
    # if request.method == 'POST':
    #     userform = UserForm(request.POST)
    #     if userform.is_valid():
    #         name = userform.cleaned_data['name']
    #         age = userform.cleaned_data['age']
    #         # tom = Person.objects.create(name="Tom", age=23)
    #         tom = Person(name=name, age=age)
    #         tom.save()
    #         change_tom = Person.objects.get(id=1)
    #         change_tom.name = name
    #         change_tom.save(update_fields=["name"])
    #         Person.objects.filter(id=2).update(name='Misha')
    #         Person.objects.filter(id=3).update(age=F('age')+5)
    #         Person.objects.update_or_create(id=3, defaults={'name': 'Maxim', 'age': 48})
    #         Person.objects.filter(id=60).delete()
    #         people = Person.objects.filter(name__startswith='e'.upper())
    #         print(people.query)
    #         mydata = Person.objects.in_bulk()
    #         # print(mydata)
    #         return render(request, "contact.html", {"form": userform, 'mydata': mydata})
    #     else:
    #         # return HttpResponse('Invalid Data')
    #         return render(request, "contact.html", {"form": userform})
    # else:
    #     userform = UserForm()
    #     langs = ["English", "German", "French", "Spanish", "Chinese"]
    #     data = {"n": 0}
    #     return render(request, "contact.html", context={'langs': langs, 'data': data, 'form': userform})


# сохранение данных в бд
def create(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            company = Company()
            company.name = request.POST.get('name')
            # tom.age = request.POST.get('age')
            company.save()
        else:
            return HttpResponse('Invalid Data')
    return HttpResponseRedirect('/')


# изменение данных в бд
def edit(request, id):
    try:
        company = Company.objects.get(id=id)

        if request.method == "POST":
            company.product_set.create(name=request.POST.get('name'), price=request.POST.get('price'))
            # person.name = request.POST.get("name")
            # person.age = request.POST.get("age")
            # person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {'company': company})
    except Company.DoesNotExist:
        return HttpResponseNotFound("<h2>Company not found</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
