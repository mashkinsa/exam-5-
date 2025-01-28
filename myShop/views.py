from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ProductForm, RegistrationForm, EditProfileForm, OrderForm
from .models import Product, Order, UserProfile
from django.contrib.auth import login, authenticate, logout


def index(request):
    if request.user.is_authenticated:
        products = Product.objects.all().order_by('-created_at')[:5]  # последние 5 товаров
        return render(request, 'index.html', {'products': products})
    else:
        return redirect('login')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


@login_required
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        order = Order(user=request.user, product=product)
        order.save()
        return redirect('profile')

    return render(request, 'product_detail.html', {'product': product})


#Регистрация
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user, avatar=form.cleaned_data['avatar'])
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('index')


def profile(request):
    user = request.user
    orders = Order.objects.filter(user=user)
    return render(request, 'profile.html', {'user': user, 'orders': orders})


@login_required
def edit_profile(request):
    user = request.user
    user_profile = user.userprofile
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            user_profile.avatar = request.FILES.get('avatar', user_profile.avatar)
            user_profile.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=user)
    return render(request, 'edit_profile.html', {'form': form})


@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('index')  # Переход на страницу со списком постов
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})
