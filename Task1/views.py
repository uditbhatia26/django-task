from django.shortcuts import render
from .models import Member
from .forms import MemberForm

# Create your views here.
def show(request):
    """
    To show all the values in the database
    """
    context = {
        "all_members": Member.objects.all
    }
    return render(request, 'show.html', context)


def join(request):
    """
    To add values in the database
    """
    if request.method == "POST":
        form = MemberForm(request.post or None)
        if form.is_valid():
            form.save()
        return render(request, 'join.html')
    else:
        return render(request, 'join.html')

