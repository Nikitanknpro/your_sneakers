from django.shortcuts import render, redirect
from django.urls import reverse
from . import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
# Create your views here.
def index(request):
    user = 'test'
    return render(request, 'main/index.html', {'user': user})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            return redirect(reverse('main:cabinet', args=()))
        else:
            return redirect(reverse('main:login_page', args=()))
    return render(request, 'main/login.html', {})



def cabinet(request):
    if request.user.is_authenticated:
        return render(request, 'main/cabinet.html', {})
    else:
        return redirect(reverse('main:login_page', args=()))


def logout_view(request):
    logout(request)
    return redirect(reverse('main:login_page', args=()))

def reqister_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        email = request.POST.get('email', None)
        firstname = request.POST.get('firstname', None)
        lastname = request.POST.get('lastname', None)
        group_id = request.POST.get('group')
        group = Group.objects.get(id=group_id)
        user = User.objects.create_user(
            username=username,
            email=email,
            first_name=firstname,
            last_name=lastname
        )
        user.set_password(password)
        user.groups.add(group)
        user.save()
        return redirect(reverse('main:login_page', args=()))
    groups = Group.objects.all()
    return render(request, 'main/register_page.html', {'groups': groups})


def products_page(request):
    products = models.Product.objects.all()
    return render(request, 'main/products.html', {'products': products})



def product_create(request):

    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        cost = request.POST.get("cost")
        cost_type = models.CostType.objects.get(id=request.POST.get("cost_type"))
        image = request.FILES.get("image")
        print(image)
        product = models.Product(
        name=name,
        description=description,
        cost=float(cost),
        cost_type=cost_type,
        image=image
        )
        product.save()
        return redirect(reverse('main:product_page', args=()))
    else:
        options = models.CostType.objects.all()
        return render(request, "main/product_create.html", {'options': options})

def product_detail(request, id):
    product = models.Product.objects.get(id=id)
    return render(request, "main/product_detail.html", {"product": product})

def brand_products(request, id):
    products = models.Product.objects.filter(brand__id=id)
    return render(request, 'main/products.html', {'products': products})

def brand_view(request):
    brands = models.Brand.objects.all()
    return render(request, 'main/brands.html', {'brands': brands})
