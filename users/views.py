from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, CuentaUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def registrate(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Te has inscrito correctamente! Ahora puedes iniciar sesion{username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def cuenta(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        c_form = CuentaUpdateForm(request.POST, request.FILES, instance=request.user.cuenta)
        if u_form.is_valid() and c_form.is_valid():
            u_form.save()
            c_form.save()
            messages.success(request, f'Tu cuenta ha sido actualizada!')
            return redirect('cuenta')
    else:
        u_form = UserUpdateForm(instance=request.user)
        c_form = CuentaUpdateForm(instance=request.user.cuenta)

    context = {
        'u_form': u_form,
        'c_form': c_form
    }

    return render(request, 'users/profile.html', context)
