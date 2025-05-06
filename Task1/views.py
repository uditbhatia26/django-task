from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Member
import json

def show(request):
    """
    Return all members as JSON.
    """
    if request.method == 'GET':
        members = list(Member.objects.values())  # Converts queryset to list of dicts
        return JsonResponse({"members": members}, safe=False)
    return JsonResponse({"error": "Only GET method allowed."}, status=405)


@csrf_exempt  # Only for development/testing – for production, handle CSRF properly
def join(request):
    """
    Add a member using JSON POST request.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            password = data.get('password')

            if not name or not email or not password:
                return JsonResponse({"error": "Missing required fields"}, status=400)

            member = Member.objects.create(name=name, email=email, password=password)
            return JsonResponse({"message": "Member created successfully", "member_id": member.id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    return JsonResponse({"error": "Only POST method allowed."}, status=405)
