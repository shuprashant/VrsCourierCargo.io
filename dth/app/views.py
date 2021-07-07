from django.shortcuts import render
from .models import Gallery
from django.core.mail import send_mail


def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            name,
            message,
            email,
            ['lavdu2020@gmail.com'],
            fail_silently=False,
        )
        return render(request, 'index.html', {'name': name})

    else:
        return render(request, 'index.html')


def air(request):
    return render(request, 'air.html')


def road(request):
    return render(request, 'road.html')


def shifting(request):
    return render(request, 'shifting.html')


def packing(request):
    return render(request, 'packing.html')


def warehouse(request):
    return render(request, 'warehouse.html')


def supply(request):
    return render(request, 'supply.html')


def gallery(request):
    gal = Gallery.objects.all()
    return render(request, 'gallery.html', {'Gallery': gal})
