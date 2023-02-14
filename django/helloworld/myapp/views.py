from django.http import JsonResponse

async def hello_world(request): 
    return JsonResponse({ "message": "Hello World" })