from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def role_redirect(request):
    if request.user.role == 'DOCTOR':
        return redirect('/doctor/add-slot/')
    elif request.user.role == 'PATIENT':
        return redirect('/patient/slots/')
    return redirect('/accounts/login/')
