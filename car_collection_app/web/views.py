from django.shortcuts import render, redirect

from car_collection_app.web.forms import CreateProfileForm, CreateCarForm, EditCarForm, DeleteCarForm, EditProfileForm, \
    DeleteProfileForm
from car_collection_app.web.models import Profile, Car


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def index(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(
        request,
        'index.html',
        context,
    )


def profile_create(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
    }
    return render(
        request,
        'profile/profile-create.html',
        context,
    )


def full_name(profile):
    first_name = profile.first_name if profile.first_name else ''
    last_name = profile.last_name if profile.last_name else ''
    return f'{first_name} {last_name}'.strip()


def price(profile):
    total_price = 0
    cars = Car.objects.all()
    for car in cars:
        total_price += car.price
    return total_price


def profile_details(request):
    profile = get_profile()
    name = full_name(profile)
    total_price = price(profile)
    context = {
        'profile': profile,
        'name': name,
        'total_price': total_price,
    }
    return render(
        request,
        'profile/profile-details.html',
        context
    )


def profile_edit(request):
    profile = get_profile()
    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    context = {
        'form': form,
        'profile': profile,
    }
    return render(
        request,
        'profile/profile-edit.html',
        context,
    )


def profile_delete(request):
    profile = get_profile()
    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile)
    else:
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
        'profile': profile,
    }
    return render(
        request,
        'profile/profile-delete.html',
        context,
    )


def catalogue(request):
    cars = Car.objects.all()
    total_cars = cars.count()
    context = {
        'cars': cars,
        'total_cars': total_cars,
        'profile': get_profile(),
    }
    return render(
        request,
        'car/catalogue.html',
        context
    )


def car_create(request):
    if request.method == 'GET':
        form = CreateCarForm()
    else:
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,
        'profile': get_profile(),
    }
    return render(
        request,
        'car/car-create.html',
        context,
    )


def car_details(request, id):
    car = Car.objects.get(pk=id)
    context = {
        'car': car,
        'profile': get_profile(),
    }
    return render(
        request,
        'car/car-details.html',
        context,
    )


def car_edit(request, id):
    car = Car.objects.get(pk=id)
    if request.method == 'GET':
        form = EditCarForm(instance=car)
    else:
        form = EditCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,
        'car': car,
        'profile': get_profile(),
    }
    return render(
        request,
        'car/car-edit.html',
        context,
    )


def car_delete(request, id):
    car = Car.objects.get(pk=id)
    if request.method == 'GET':
        form = DeleteCarForm(instance=car)
    else:
        form = DeleteCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    context = {
        'form': form,
        'car': car,
        'profile': get_profile(),
    }
    return render(
        request,
        'car/car-delete.html',
        context,
    )

