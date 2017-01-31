'''
Dummy signin/signup methods.
There are no validation, or proper error handling, and there is
a simple basic auth to protect private resources.
'''

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import FrontUser
from .utils import basicauth
import bcrypt
import json


@csrf_exempt
def signin(request):
    '''
    Dummy signin: check email/password in database.
    Success: 200
    Failure: 401 (email not found, password incorrect)
    '''
    data = json.loads(request.body)
    email = data['email']
    raw_password = data['password']

    user = None
    try:
        user = FrontUser.objects.get(email=email)
    except FrontUser.DoesNotExist:
        return HttpResponse({}, status=401, content_type='application/json')

    result = bcrypt.hashpw(raw_password, user.password) == user.password

    if result:
        return HttpResponse({}, content_type='application/json')

    return HttpResponse({}, status=401, content_type='application/json')


@csrf_exempt
def signup(request):
    '''
    Dummy signup: check if the email already exists
    Success: 201
    Failure: 409 email already exists
    '''
    data = json.loads(request.body)
    email = data['email']
    raw_password = data['password']
    first_name = data.get('first_name', '')
    last_name = data.get('last_name', '')

    user = None
    try:
        user = FrontUser.objects.get(email=email)
    except FrontUser.DoesNotExist:
        pass

    if user is not None:
        json_data = json.dumps({'error': 'Email already exists'})
        return HttpResponse(
            json_data,
            status=409,
            content_type='application/json'
        )

    hashed_password = bcrypt.hashpw(raw_password, bcrypt.gensalt())

    user = FrontUser(
        email=email,
        password=hashed_password,
        first_name=first_name,
        last_name=last_name
    )

    user.save()

    return HttpResponse({}, status=201, content_type='application/json')


@csrf_exempt
@basicauth
def change_password(request):
    data = json.loads(request.body)
    raw_password = data['password']

    hashed_password = bcrypt.hashpw(raw_password, bcrypt.gensalt())

    request.user.password = hashed_password

    request.user.save()

    return HttpResponse({}, status=200, content_type='application/json')


@csrf_exempt
@basicauth
def profile(request):
    json_data = json.dumps(request.user.to_view())
    return HttpResponse(json_data, content_type='application/json')
