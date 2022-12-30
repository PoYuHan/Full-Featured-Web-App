from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterFrom

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            # save the data to DB
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your account has been created! You can log in now!!")
            return redirect('login')

    else:
        form = UserRegisterFrom()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')


# messages.debug
# messages.info
# messages.success