from django.shortcuts import render, redirect, get_object_or_404
from . forms import UserRegistrationForm, UserProfileForm, ProfilePictureForm, ClientAddForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .models import Client


# Create your views here.
def index(request):
    return render(request, 'users/index.html', {})


def login_required(fn):
    def wrapper(request,*args,**kwargs):
        if request.user.is_anonymous:
            messages.success(request,"Sorry! You are not logged in. You have to login to access this page.")
            return redirect("users-login")
        else:
            return fn(request,*args,**kwargs)
    return wrapper



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Registration success for {username}')
            return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, instance=request.user)
        profile_picture_form = ProfilePictureForm(request.POST,
                                                  request.FILES,
                                                  instance=request.user.profile)
        if user_form.is_valid() and profile_picture_form.is_valid():
            user_form.save()
            profile_picture_form.save()
            username = user_form.cleaned_data.get('username')
            messages.success(request, f'Profile updated for the user {username}')
            return redirect('users-profile')

    else:
        user_form = UserProfileForm(instance=request.user)
        profile_picture_form = ProfilePictureForm()
    return render(request, 'users/profile.html',
                  {'user_form': user_form,
                   'profile_picture_form': profile_picture_form})



def logout_user(request):
    logout(request)
    messages.success(request, ('You Have Been Logged Out!!!'))
    return redirect("index")


class UserPasswordChangeView(PasswordChangeView):
    model = User
    template_name = 'users/password_change_form.html'
    success_url = reverse_lazy('users-profile')

    def form_valid(self, form):
        messages.success(self.request, 'Your password has been changed.')
        return super().form_valid(form)



def clients(request):
    if request.method == 'POST':
        data = request.POST
        client_pic = request.FILES.get('client_pic')
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        email = data.get('email')
        mobile = data.get('mobile')

        Client.objects.create(
            client_pic=client_pic,
            firstname=firstname,
            lastname=lastname,
            email=email,
            mobile=mobile,
        )
        messages.success(request, f'Client created for the email {email}')
        return redirect('clients')

    queryset = Client.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(email__icontains=request.GET.get('search'))

    context = {'clients': queryset}
    return render(request, 'users/clients.html', context)


def update_client(request, id):
    client = get_object_or_404(Client, id=id)
    if request.method == 'POST':
        data = request.POST
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        email = data.get('email')
        mobile = data.get('mobile')
        client_pic = request.FILES.get('client_pic')


        client.firstname = firstname
        client.lastname = lastname
        client.email = email
        client.mobile = mobile
        if client_pic:
            client.client_pic = client_pic
        client.save()
        messages.info(request, f'Client updated for the email {email}')
        return redirect('clients')

    context = {'client': client}
    return render(request, 'users/update_client.html', context)



def delete_client(request, id):
    client = get_object_or_404(Client, id=id)
    client.delete()
    messages.error(request, 'Client deleted')
    return redirect('clients')


def show_client(request, id):
    client = get_object_or_404(Client, id=id)
    context = {'client': client}
    return render(request, 'users/show_client.html', context)