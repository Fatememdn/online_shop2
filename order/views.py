from .models import *
import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from accounts.models import User
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

def add_product_to_cart(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_number = data['number']
            product_id = int(data['product_id'])
            quantity1 = int(data['quantity'])
            product1 = Product.objects.get(id=product_id)
            user1 = User.objects.get(phone=user_number)
            user_order, created = UserOrder.objects.get_or_create(user=user1)
            order_detail, created = OrderDetail.objects.get_or_create(
                order=user_order,
                product=product1
            )
            if created:
                order_detail.quantity = quantity1
            else:
                order_detail.quantity += quantity1
            order_detail.save()

            return JsonResponse({'message': 'Product added to cart successfully'})

        except User.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'})
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product does not exist'})
        except Exception as e:
            return JsonResponse({"error": str(e)})
    else:
        return JsonResponse({'error': 'Invalid request method'})


def view_cart(request, user_id):
    try:
        result = []
        user = get_object_or_404(User, id=user_id)
        order = get_object_or_404(UserOrder, user=user)
        order_details = OrderDetail.objects.filter(order=order)

        for order_detail in order_details:
            product = order_detail.product
            product_dict = {
                'name': product.name,
                'quantity': order_detail.quantity,
                'total_price': product.price * order_detail.quantity
            }
            result.append(product_dict)

        return JsonResponse(result, safe=False)
    except Exception as e:
        return JsonResponse({"error: ", str(e)}, safe=False)





