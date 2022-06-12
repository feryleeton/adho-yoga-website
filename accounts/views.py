from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from accounts.forms import SignUpForm, LoginForm, ProfileForm
from adho_yoga import settings
from accounts.models import AdhoUser


class RegisterUser(CreateView):
    form_class = SignUpForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    success_url = 'home'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('home')


class UserProfile(DetailView):
    model = AdhoUser
    context_object_name = 'user'
    template_name = 'accounts/profile.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_form'] = ProfileForm()
        return context

    def get_object(self, *args, **kwargs):
        return self.request.user

    @staticmethod
    def post(request, pk):
        pk = request.user.pk
        user = AdhoUser.objects.get(pk=pk)

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        if not AdhoUser.objects.filter(username=request.POST['username']):
            user.username = request.POST['username']
        user.email = request.POST['email']
        user.mobile_number = request.POST['mobile_number']

        user.country = request.POST['country']
        user.state = request.POST['state']
        user.postal_code = request.POST['postal_code']
        user.address = request.POST['address']

        user.save()

        form = ProfileForm()
        return render(request, 'accounts/profile.html', {
            'profile_form': form,
            'user': user,
        })


def logout_user(request):
    logout(request)
    return redirect('home')