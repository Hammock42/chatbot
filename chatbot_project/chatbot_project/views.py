from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
import json



@csrf_exempt
def api(request):
    
    if request.method == 'POST':
        data = json.loads(request.body)
        user_msg = data['message']
        ## ai_msg = get_ai_response(user_msg)
        ai_msg = "Hello, I am a chatbot. How can I help you?"
        resp = {'message': ai_msg}
    return JsonResponse(resp) 