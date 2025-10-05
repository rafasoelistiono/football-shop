import datetime
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from main.forms import ProductForm
from main.models import Product

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")
    category_filter = request.GET.get("category", None)
    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    if category_filter:
        product_list = product_list.filter(category=category_filter)

    context = {
        'app_name': 'AthleteLab',
        'name': 'Rafa Rally Soelistiono',
        'class': 'PBP D',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, 'main.html', context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_sales()

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id' : str(product.id),
            'name' : product.name,
            'description' : product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'sales_count' : product.sales_count,
            'stock' : product.stock,
            'price' : product.price,
            'rating' : product.rating,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
        }
        for product in product_list
    ]
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
   try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
   try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id' : str(product.id),
            'name' : product.name,
            'description' : product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'sales_count' : product.sales_count,
            'stock' : product.stock,
            'price' : product.price,
            'rating' : product.rating,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username' : product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
   except Product.DoesNotExist:
        return HttpResponse({'detail' :'Not Found'},status=404)
   
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        messages.success(request, f'Welcome back, {user.username}!')
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
      else:
        messages.error(request, 'Invalid username or password.')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully!')
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    news = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=news)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = request.POST.get("name")
    description = request.POST.get("description")
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    stock = request.POST.get("stock", 0)
    price = request.POST.get("price", 0)
    rating = request.POST.get("rating", 0.0)
    is_featured = request.POST.get("is_featured") == 'on'
    user = request.user if request.user.is_authenticated else None

    new_product = Product(
        name=name,
        description=description,
        category=category,
        thumbnail=thumbnail,
        stock=stock,
        price=price,
        rating=rating,
        is_featured=is_featured,
        user=user,
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_product_ajax(request, id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return JsonResponse({"status": "deleted"}, status=200)
    except Product.DoesNotExist:
        return HttpResponseNotFound("Product not found")
    

@csrf_exempt
def edit_product_ajax(request, id):
    product = get_object_or_404(Product, pk=id)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            updated_product = form.save()
            return JsonResponse({
                "id": str(updated_product.id),
                "name": updated_product.name,
                "description": updated_product.description,
                "category": updated_product.category,
                "thumbnail": updated_product.thumbnail,
                "price": updated_product.price,
                "stock": updated_product.stock,
                "is_featured": updated_product.is_featured,
                "user_id": updated_product.user.id,
            })
        else:
            return JsonResponse({"errors": form.errors}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=400)


