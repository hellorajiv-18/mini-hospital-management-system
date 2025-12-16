from django.core.exceptions import PermissionDenied

def doctor_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.role != 'DOCTOR':
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return wrapper


def patient_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.role != 'PATIENT':
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return wrapper
