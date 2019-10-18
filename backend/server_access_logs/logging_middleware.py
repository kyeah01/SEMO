from .models import AccessLogsModel
from django.conf import settings
from django.utils import timezone

from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

class AccessLogsMiddleware(object):

    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        # create session
        if not request.session.session_key:
            request.session.create()
        # Getting user using session
        session_key = request.session.session_key
        session = Session.objects.get(session_key=session_key)
        uid = session.get_decoded().get('_auth_user_id')
        user = User.objects.get(pk=uid)

        access_logs_data = dict()

        # get the request path
        access_logs_data["path"] = request.path

        # get the client's IP address
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        access_logs_data["ip_address"] = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')
        access_logs_data["method"] = request.method
        access_logs_data["referrer"] = request.META.get('HTTP_REFERER',None)
        # django session key
        access_logs_data["session_key"] = request.session.session_key
        access_logs_data["user"] = user.username

        data = dict()
        data["get"] = dict(request.GET.copy())
        data['post'] = dict(request.POST.copy())

        # remove password form post data for security reasons
        keys_to_remove = ["password", "csrfmiddlewaretoken"]
        for key in keys_to_remove:
            data["post"].pop(key, None)

        access_logs_data["data"] = data
        access_logs_data["timestamp"] = timezone.now()
        try:
            AccessLogsModel(**access_logs_data).save()
        except Exception as e:
            pass

        response = self.get_response(request)
        return response