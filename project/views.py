from django.http import JsonResponse
from django.shortcuts import render
def chatbot_ui(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        # Here you can add your logic for NLP to SQL query conversion
        # For now, let's just respond with a static message
        response = "tell me how can i help you"
        return JsonResponse({'response': response})
    return render(request, 'project/chatbot_ui.html')
