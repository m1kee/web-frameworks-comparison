from django.http import JsonResponse
from django.db import connections

async def hello_world(request): 
    return JsonResponse({ "message": "Hello World" })

def get_users(request):
    with connections['test'].cursor() as cursor:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
    return JsonResponse(users, safe=False)