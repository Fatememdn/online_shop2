from .models import *
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def add_user(requst):
    if requst.method == 'POST':
        try:
            data = json.loads(requst.body)
            name = data['name']
            phone = data['phone']
            email = data['email']
            address = data['address']
            if User.objects.filter(email = email).exists():
                return JsonResponse({"message": "Email already exists"})
            elif User.objects.filter(phone = phone).exists():
                return JsonResponse({"message": "Username already exists"})
            else:
                new_user = User.objects.create(name= name , 
                                      phone = phone,
                                      address=address,
                                      email=email)
                new_user.save()
                return JsonResponse({"message": "Costumer added successfully"})
        except Exception as e:
            return JsonResponse({"error": str(e)})
    else:
        return JsonResponse({'error': 'Invalid request method'})
        
def user_list(request):
    user_list = User.objects.all()
    result = []
    for user in user_list:
        user_dict = {
            'name' : user.name, 
            'email' : user.email,
            'phone' : user.phone,
            'address': user.address,}
        result.append(user_dict)
    return JsonResponse(result, safe=False)

