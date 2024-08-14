from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib import auth
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST

from .forms import SignupForm


class Login(View):
    template_name = 'registration/login.html'

    def get(self, request):
        
        return render(request, template_name=self.template_name)

    def post(self, request):
        user = auth.authenticate(request,
                                 username=request.POST.get('username'),
                                 password=request.POST.get('password'),
                                 )
        if user is not None:
            auth.login(self.request, user)
            # messages.success(self.request, 'you are login')
            return redirect('page:home')
        else:
            # messages.error(self.request,
            #                format_html('The password is wrong or you have not registered. if you signup click <a href="{}">Sing Up</a>'.format(reverse('account:signup'))))
            return redirect('page:home')


class Signup(View):
    
    @method_decorator(require_POST)
    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            user = auth.authenticate(request, username=request.POST.get('username'), password=request.POST.get('password1'))
            auth.login(request, user=user)
            return redirect('page:home')
        else:
            return redirect('account:login')
        


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.success(request, 'You are logout')
    return redirect('page:home')

