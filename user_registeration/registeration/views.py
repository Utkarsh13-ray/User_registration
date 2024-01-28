from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')

        if not (username and email and password and confirm_password):
            return JsonResponse({'error': 'Please fill out all fields.'}, status=400)

        if password != confirm_password:
            return JsonResponse({'error': 'Passwords do not match.'}, status=400)

        if User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email is already in use.'}, status=400)

        user = User.objects.create_user(username=username, email=email, password=password)


        mail_content = f'Username: {username}\nEmail: {email}\nPassword: {password}'
        send_mail(
            'User Registration',
            mail_content,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        return JsonResponse({'success': 'User registered successfully!'})

    return render(request, 'registration/register.html')
