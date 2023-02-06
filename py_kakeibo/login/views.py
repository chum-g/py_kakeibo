from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def login(request):
    context = {}

    if request.method != "POST" :
        return render(request, 'login/login.html', context)
    
    # どっちでも可
    login_id       = request.POST.get('login_id')
    login_password = request.POST["login_password"]
    post = request.POST

    context = {'login_id': login_id, 'login_password': login_password, 'post': post}
    # return render(request, 'detail/detail_month.html', context)
    return render(request, 'login/login.html', context)

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
                login_user(request, new_user)
                return redirect("detail:index")
    else:
        form = UserCreationForm()
    return render(request, "login/signup.html", {"form": form})


def login_user(request, user):
    return