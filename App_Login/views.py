from django.shortcuts import render,HttpResponseRedirect
from .forms import CreateNewUser,LogInForm,UserProfileChange,ProfilePic
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.

def sign_up(request):
    form = CreateNewUser()
    registered = False
    if request.method == "POST":
        form = CreateNewUser(data = request.POST)

        if form.is_valid():
            form.save()
            registered = True
            return HttpResponseRedirect(reverse('App_Login:login'))
    
    diction = {'form':form,'registered':registered}
    return render(request,'App_Login/signup.html',context=diction)

def login_page(request):
    form = LogInForm()
    if request.method=="POST":
        form = LogInForm(data = request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user =  authenticate(username = username,password=password)

            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
    
    diction = {'form':form}
    return render(request,'App_Login/login.html',context = diction)


@login_required

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required

def profile(request):
    return render(request,'App_Login/profile.html',context = {})


@login_required

def user_change(request):
    current_user = request.user #jei user er data update korte chi take ei current_user er moddeh reke diyechi
    form = UserProfileChange(instance=current_user)

    if request.method =="POST":
        form = UserProfileChange(request.POST,instance=current_user)

        if form.is_valid():
            form.save()
            form = UserProfileChange(instance=current_user) #update value gula abar jate page e show kore tai eti use kora hoy!
    return render(request,'App_Login/change_profile.html',context = {'form':form})


@login_required
def pass_change(request):
    current_user = request.user
    changed = False
    form = PasswordChangeForm(current_user)
    if request.method=="POST":
        form = PasswordChangeForm(current_user,data = request.POST)

        if form.is_valid():
            form.save()
            changed = True
    
    return render(request,'App_Login/change_pass.html',context={'form':form,'changed':changed})


@login_required

def add_pro_pic(request):
    form = ProfilePic()
    if request.method =="POST":
        form = ProfilePic(request.POST,request.FILES)
        if form.is_valid():
            user_obj = form.save(commit = False)
            user_obj.user = request.user 
            user_obj.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))

    return render(request,'App_Login/pro_pic_add.html',context = {'form':form})


def change_pro_pic(request):
    form = ProfilePic(instance=request.user.user_profile)
    if request.method =="POST":
        form = ProfilePic(request.POST,request.FILES,instance = request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request,'App_Login/pro_pic_add.html',context = {'form':form})

            
    




