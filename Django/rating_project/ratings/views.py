from django.shortcuts import render, redirect
from .models import Object
from django.http import JsonResponse

def index(request):
    objects = Object.objects.all()
    return render(request, 'ratings/index.html', {'objects': objects})

def add_object(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Object.objects.create(name=name)
    return redirect('index')

def rate_object(request, object_id):
    if request.method == 'POST':
        rating_value = request.POST.get('rating')
        object_to_rate = Object.objects.get(pk=object_id)
        user = request.user

        # Тук може да добавите или изтриете рейтинг в зависимост от стойността на rating_value
        # Например, ако rating_value е 'plus', увеличете рейтинга; ако е 'minus', намалете рейтинга

    return redirect('index')

def average_rating(request, object_id):
    object_to_rate = Object.objects.get(pk=object_id)

    # Изчислете средния рейтинг на обекта и го върнете като JSON отговор
    total_rating = object_to_rate.ratings.aggregate(models.Avg('rating'))
    return JsonResponse({'average_rating': total_rating['rating__avg']})


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

