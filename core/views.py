from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SignUpForm




# Create your views here.
def frontpage(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        # ip = request.META.get('REMOTE_ADDR')
        ip = 'this user is protected'
        print('\n\n\nHis IP address is: ' + ip + '\n\n')
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid:
            user = form.save()

            login(request, user)
            return redirect('frontpage')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})

