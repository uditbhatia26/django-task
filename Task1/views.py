from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .db import SessionLocal
from .models_sqlalchemy import Member
import os

@csrf_exempt
def join(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        file = request.FILES.get('file')

        if not name or not email or not password:
            return JsonResponse({"error": "Missing required fields"}, status=400)

        session = SessionLocal()

        # Handle file saving
        file_path = None
        if file:
            save_path = os.path.join('uploads', file.name)
            with open(save_path, 'wb+') as f:
                for chunk in file.chunks():
                    f.write(chunk)
            file_path = save_path

        member = Member(name=name, email=email, password=password, file=file_path)
        session.add(member)
        session.commit()
        session.refresh(member)
        session.close()

        return JsonResponse({
            "message": "Member created successfully",
            "member_id": member.id,
            "file": member.file
        }, status=201)

    return JsonResponse({"error": "Only POST method allowed."}, status=405)


def show(request):
    if request.method == 'GET':
        session = SessionLocal()
        members = session.query(Member).all()
        session.close()
        members_list = [
            {
                "id": m.id,
                "name": m.name,
                "email": m.email,
                "file": m.file
            } for m in members
        ]
        return JsonResponse({"members": members_list})
    return JsonResponse({"error": "Only GET method allowed."}, status=405)
