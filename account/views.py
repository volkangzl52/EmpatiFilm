from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_encode
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from .forms import SignUpForm
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode
from django.shortcuts import redirect
from django.contrib.auth.tokens import default_token_generator
from django.views.generic import View
from django.shortcuts import render, redirect
from .models import Survey, Answer

class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_bytes(urlsafe_base64_decode(uidb64))
            user = get_user_model().objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            
            user.is_active = True
            user.save()
            
            return redirect('login')
        else:
            
            return HttpResponse("Activation link is invalid or expired")

class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False  
        user.save()

        
        current_site = get_current_site(self.request)
        mail_subject = 'Activate your account'
        message = render_to_string('registration/account_activation_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': PasswordResetTokenGenerator().make_token(user),
        })
        to_email = form.cleaned_data.get('email')
        
      
        send_mail(mail_subject, message, settings.DEFAULT_FROM_EMAIL, [to_email])

        return HttpResponse('Please confirm your email address to complete the registration')
    

def survey(request):
    if request.method == 'POST':
        
        answer1 = request.POST.get('question1')
        answer2 = request.POST.get('question2')
        answer3 = request.POST.get('question3')
        
        
        if answer1 == 'A' and answer2 == 'A' and answer3 == 'A':
            movie_genre = 'Romantic'
        elif answer1 == 'A' and answer2 == 'A' and answer3 == 'B':
            movie_genre = 'Comedy'
        elif answer1 == 'A' and answer2 == 'B' and answer3 == 'B':
            movie_genre = 'Adventure'
        elif answer1 == 'B' and answer2 == 'A' and answer3 == 'A':
            movie_genre = 'Romantic Comedy'
        elif answer1 == 'B' and answer2 == 'B' and answer3 == 'B':
            movie_genre = 'Action'
        elif answer1 == 'B' and answer2 == 'A' and answer3 == 'B':
            movie_genre = 'Gerilim'
        else:
            
            return render(request, 'failed.html')


        return render(request, 'recommended_movies.html', {'movie_genre': movie_genre})
    else:
        return render(request, 'survey.html')
    
