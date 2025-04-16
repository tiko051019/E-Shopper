from django.utils.timezone import now
from dashboard.models import *

class ActiveUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            activity, _ = UserActivity.objects.get_or_create(user=request.user)
            activity.last_activity = now()
            activity.save(update_fields=["last_activity"])

        return response
    