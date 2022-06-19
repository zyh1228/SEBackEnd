from django.utils.deprecation import MiddlewareMixin
from django.utils.timezone import now

from seBackEnd import settings
from utils.shortcuts import datetime2str


class SessionRecordMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.ip = request.META.get(settings.IP_HEADER, request.META.get("REMOTE_ADDR"))
        if request.user.is_authenticated:
            session = request.session
            session["user_agent"] = request.META.get("HTTP_USER_AGENT", "")
            session["ip"] = request.ip
            session["last_activity"] = datetime2str(now())

            request.user.session_key = session.session_key
            request.user.save()
