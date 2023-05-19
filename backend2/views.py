import json
from django.http import JsonResponse

def process_price(request):
    print(request)
    if request.method == "POST":
        data = json.loads(request.body)
        price = data["price"]
        print("KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK")
        print(price)

        # Process the price as needed

        return JsonResponse({"status": "success"})
