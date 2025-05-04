from django.shortcuts import render, HttpResponse
from .models import Member
from .forms import MemberForm

# Create your views here.

context = {
        "all_members": Member.objects.all
    }

def show(request):
    """
    To show all the values in the database
    """
    return render(request, 'show.html', context)


def join(request):
    """
    To add values in the database
    """
    if request.method == "POST":
        form = MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'show.html', context)
    else:
        return render(request, "join.html")

