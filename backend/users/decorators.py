from django.http import HttpResponseForbidden
from functools import wraps


def patient_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == 'PATIENT':
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden()
    return _wrapped_view


def doctor_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == 'DOCTOR':
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden()
    return _wrapped_view

