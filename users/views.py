from django.utils.html import escape
import json
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotAllowed, HttpResponseBadRequest, JsonResponse
from django.contrib.auth import authenticate, login, logout
from .forms import EditProfileForm, UserForm, LoginForm, RegisterForm, PasswordForgot, PasswordChange, ROLES
from django.contrib.auth.models import User, make_password, Group, Permission
from django.views.decorators.csrf import csrf_exempt
import jwt
from django.conf import settings
from datetime import datetime, timedelta, timezone
from.models import Profile
from django.middleware.csrf import get_token


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def ping_pong(request):
    if request.method == 'GET':
        return JsonResponse({"message":"Pong"}, status=200)
    else:
        return JsonResponse({"error":"Method not allowed"}, status=405)
    
def user_register(request, next = ''):
    if request.method == 'POST':
        if User.objects.filter(email=request.POST['email']).exists():
            return HttpResponse('User already exists')
        user = User()
        user.username = request.POST['email']
        user.email = request.POST['email']
        user.last_name = request.POST['last_name']
        user.first_name = request.POST['first_name']
        user.password = make_password(request.POST['password'])
        user.save()

        if Group.objects.count() == 0:
            Group.objects.create(name='Administrator')
            Group.objects.create(name='Customer')
            Group.objects.create(name='Attendant')
            Group.objects.create(name='Organisator')
        # Add user to group Contact. Add first user to Group Administrator
        if User.objects.count() == 1:
            group = Group.objects.get(name='Administrator')
            user.is_staff = True
            user.is_superuser = True
            user.save()
        else:
            group = Group.objects.get(name='Customer')
        group.user_set.add(user)
        
        profile = user.profile
        profile.bike = request.POST['bike']
        profile.save()
        login(request, user)
        token = jwt.encode({'user_id': user.id, 'exp': datetime.now() + timedelta(days=2)}, settings.SECRET_KEY, algorithm='HS256')

        return JsonResponse({"message":"Success", "data":user}, status=200)
            
    else:
        return JsonResponse({"error":"Method not allowed"}, status=405)

def user_login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['email'], password=request.POST['password'])
        if user and user.is_authenticated:
            login(request, user)
            return send_user_info(request)
        else:
            return JsonResponse({"error":"Forbidden", "message":"Invalid email or password."}, status=403)
    else:
        # if request.user is not None:
        #     HttpResponse('what?')
        # else:
        return JsonResponse({"error":"Method not allowed"}, status=405)
    
def check_authentication(request):
    if request.method == 'GET':
        auth_header = request.COOKIES.get('auth_token')
        print(auth_header)
        if auth_header:
            # Decode the token
            payload = jwt.decode(auth_header, settings.SECRET_KEY, algorithms=['HS256'])
            # Check if the token is expired
            if 'exp' in payload and datetime.now() > datetime.fromtimestamp(payload['exp']):
                return JsonResponse({"error":"Forbidden", "message":"Token expired."}, status=403)
            # If the token is valid, set the user
            user = User.objects.get(id=payload['user_id'])
            request.user = user
            login(request, user)
            return send_user_info(request)
        else:
            csrf_token = get_token(request)
            # Create a JsonResponse with the CSRF token in the headers
            response = JsonResponse({"message": "Pong"})
            response['X-CSRFToken'] = csrf_token
            return response
    else:
        return JsonResponse({"error":"Method not allowed"}, status=405)

def user_logout(request):
    logout(request)
    return JsonResponse({"message":"Logout success"}, status=200)

def send_user_info(request):
    profile = Profile.objects.get(user = request.user)
    # Escape user-generated content to prevent XSS
    escaped_username = escape(profile.user.username)
    escaped_firstname = escape(profile.user.first_name)
    escaped_lastname = escape(profile.user.last_name)
    escaped_bike = escape(profile.bike)
    # Generate a token with a TTL of 2 days
    token = jwt.encode({'user_id': profile.user.id, 'exp': datetime.now() + timedelta(days=2)}, settings.SECRET_KEY, algorithm='HS256')
    
    # Set the token in a cookie
    response = JsonResponse({"message":"Success","data":{
        "username": escaped_username,
        "firstname": escaped_firstname,
        "lastname": escaped_lastname,
        "bike": escaped_bike}}, status=200)
    response.set_cookie('auth_token', token, httponly=True, samesite='Lax', secure=True)
    
    return response

