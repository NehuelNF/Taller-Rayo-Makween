from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps


def staff_required(view_func):
    @wraps(view_func)
    def _wrapped_view_func(request, *args, **kwargs):
        if not request.user.is_staff:
            messages.error(request, 'Usted no cuenta con los permisos necesarios')
            response = redirect('paginaPrincipal')
            response['Location'] += '?redirected=true'
            return response
        return view_func(request, *args, **kwargs)
    return _wrapped_view_func

def superuser_required(view_func):
    @wraps(view_func)
    def _wrapped_view_func(request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, 'Usted no cuenta con los permisos necesarios')
            response = redirect('paginaPrincipal')
            response['Location'] += '?redirected=true'
            return response
        return view_func(request, *args, **kwargs)
    return _wrapped_view_func