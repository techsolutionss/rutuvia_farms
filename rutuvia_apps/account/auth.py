from .models import Account
from django.middleware.csrf import rotate_token
from django.utils.crypto import salted_hmac, constant_time_compare

#1 
def user_authenticate(form_data):
    try:
        user = Account.objects.get(**form_data)
        return user
    except Account.DoesNotExist:
        return None

def get_user_session_id(request):
    if "USER_SESSION_ID" in request.session:
        return request.session.get("USER_SESSION_ID", None)
    else:
        return None

def calculate_user_session_hash(value):
    key_salt = "rutuvia_apps.accounts.auth.get_user_session_hash"
    return salted_hmac(key_salt, value).hexdigest()


def user_login(request, user):
    if "USER_SESSION_ID" in request.session:
        if get_user_session_id(request) != user.id:
            request.session.flush()
            try:
                del request.session['USER_SESSION_ID']
            except KeyError:
                pass
    else:
        request.session.cycle_key()

    request.session["USER_SESSION_ID"] = user.id
    rotate_token(request)

def user_logout(request):
    try:
        del request.session['USER_SESSION_ID']
    except KeyError:
        pass


def user_is_authenticated(request):
    user_session_id = get_user_session_id(request)
    if user_session_id:
        user = Account.objects.get(pk=user_session_id)
        return user
    else:
        return None