from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Member
import json

def show(request):
    """
    Return all members as JSON.
    """
    if request.method == 'GET':
        members = list(Member.objects.values())
        return JsonResponse({"members": members}, safe=False)
    return JsonResponse({"error": "Only GET method allowed."}, status=405)


@csrf_exempt
def join(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        file = request.FILES.get('file')  

        if not name or not email or not password:
            return JsonResponse({"error": "Missing required fields"}, status=400)

        member = Member.objects.create(
            name=name,
            email=email,
            password=password,
            file=file
        )

        return JsonResponse({
            "message": "Member created successfully",
            "member_id": member.id,
            "file_url": member.file.url if member.file else None
        }, status=201)

    return JsonResponse({"error": "Only POST method allowed."}, status=405)