from django.shortcuts import render
import json 
from .models import Book
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index_view(request):
    return render(request, "index.html")

@csrf_exempt
def save_json(request):
    if request.method == 'POST':
        try:
            payload = json.loads(request.body)
            name = payload.get('name')
            author_name = payload.get('author_name')
            language = payload.get('language')  # Corrected typo
            price = payload.get('price')
            
            if name and author_name and language and price:  # Add a check for required fields
                book = Book.objects.create(
                    name=name,
                    author_name=author_name,
                    language=language,
                    price=price
                )
                return HttpResponse('Json Data has been saved successfully')
            else:
                return HttpResponse('Missing fields in the JSON data', status=400)
        except json.JSONDecodeError:
            return HttpResponse('Invalid JSON', status=400)
    else:
        return HttpResponse('Only POST requests are allowed', status=405)
