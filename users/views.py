from email.message import EmailMessage
from django.core.mail import EmailMessage
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.core.mail import send_mail

from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm


class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        response = super().form_valid(form)


        email = EmailMessage(
            subject="Добро пожаловать!",
            body=f"Привет, {self.object.email}! Спасибо за регистрацию.",
            to=[self.object.email]
        )
        email.send(fail_silently=False)
        return response


class UserLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'users/login.html'
