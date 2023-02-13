from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # ユーザーを認証する
            new_user = authenticate(username=username, password=raw_password) 
            if new_user is not None:
                # ユーザーをログイン状態にする
                login(request, new_user)
                return redirect("notification:notification")
    else:
        form = UserCreationForm()
    return render(request, "login/signup.vue", {"form": form})

def login(request):
    cont = request.POST
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                return redirect("notification:notification")
    else:
        # form = LoginForm()
        form = 0

    return render(request, 'login/login.vue', {"form": form, "cont": cont})

def index(request):
    return redirect("notification:notification")
    # return 
