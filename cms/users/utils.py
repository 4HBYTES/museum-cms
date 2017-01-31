'''
Source: https://djangosnippets.org/snippets/243/
'''
from .models import FrontUser
from django.http import HttpResponse
from functools import wraps
import base64
import bcrypt


def basicauth(view):
  @wraps(view)
  def view_or_basicauth(request, *args, **kwargs):
    if 'HTTP_AUTHORIZATION' in request.META:
        auth = request.META['HTTP_AUTHORIZATION'].split()
        if len(auth) == 2:
            if auth[0].lower() == "basic":
                uname, passwd = base64.b64decode(auth[1]).split(':')

                user = None
                try:
                    user = FrontUser.objects.get(email=uname)
                except FrontUser.DoesNotExist:
                    return HttpResponse(status=401)

                result = bcrypt.hashpw(passwd, user.password) == user.password
                if not result:
                    return HttpResponse(status=401)

                request.user = user
                return view(request, *args, **kwargs)

    return HttpResponse(status=401)

  return view_or_basicauth
