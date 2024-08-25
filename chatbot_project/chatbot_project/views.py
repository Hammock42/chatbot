from django.http import JsonResponse

def api(request):
    test_response = {"message": "Hello, world!"}
    return JsonResponse(test_response)