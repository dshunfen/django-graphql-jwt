import pickle
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class MyVulnerableView(View):

    def insecure_deserialization_view(request):
        user_data = request.GET.get('data')
        deserialized_data = pickle.loads(user_data.encode('latin1'))
        return HttpResponse(f"Deserialized data: {deserialized_data}")

    def xss_vulnerable_view(request):
        user_input = request.GET.get('user_input', '')
        return HttpResponse(f"Your input was: {user_input}")

