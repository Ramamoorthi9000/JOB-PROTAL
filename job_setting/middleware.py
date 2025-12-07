from django.urls import reverse
from django.shortcuts import redirect


class RedirectAuthenticatedUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # If user is already logged in
        if request.user.is_authenticated:
            paths_to_redirect = [
                reverse('lf:loginn'),
                reverse('lf:register')
            ]

            if request.path in paths_to_redirect:
                return redirect(reverse('job:dash'))

        return self.get_response(request)


class RestrictUnauthenticateUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        restricted_paths = [
            reverse('job:dash')
        ]

        # Block unauthenticated users from protected pages
        if not request.user.is_authenticated and request.path in restricted_paths:
            return redirect(reverse('lf:loginn'))

        return self.get_response(request)
