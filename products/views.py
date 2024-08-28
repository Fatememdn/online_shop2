from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product, Category
import json

def product_list(request):  
    products = Product.objects.all()
    result = []
    for item in products:
        product_dict = {
            'name': item.name,
            'category': list(item.category.values_list('title', flat=True)),
            'price': item.price,
            'description': item.description,
        }
        result.append(product_dict)
    return JsonResponse(result, safe=False)

def search_product_by_name(request, name):
    products = Product.objects.filter(name__icontains=name)
    result = []
    for item in products:
        product_dict = {
            'name': item.name,
            'category': list(item.category.values_list('title', flat=True)),
            'price': item.price,
            'description': item.description,
        }
        result.append(product_dict)
    return JsonResponse(result, safe=False)

def search_product_by_category(request, category):
    products = Product.objects.filter(category__title__icontains=category).distinct()
    result = []
    for item in products:
        product_dict = {
            'name': item.name,
            'category': list(item.category.values_list('title', flat=True)),
            'price': item.price,
            'description': item.description,
        }
        result.append(product_dict)
    return JsonResponse(result, safe=False)

@csrf_exempt
def add_product(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data['name']
            category_title = data['category']
            price = data['price']
            description = data['description']
            stock = data['stock']
            
            category = Category.objects.get(title=category_title)
            
            if Product.objects.filter(name=name).exists():
                return JsonResponse({"message": "A product with this name already exists."}, status=400)
            
            product = Product.objects.create(
                name=name,
                price=price,
                description=description,
                stock=stock
            )
            
            product.category.add(category)
            
            return JsonResponse({"message": "Product added successfully"}, status=201)
        
        except Category.DoesNotExist:
            return JsonResponse({"error": "Category does not exist."}, status=400)
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
        



    