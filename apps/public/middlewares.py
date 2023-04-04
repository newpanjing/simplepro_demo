from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin


class PasswordChangeMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.path == '/password_change/':
            return render(request, 'password_change.html')
