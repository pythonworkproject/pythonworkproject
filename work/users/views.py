from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout,login
from django.http import HttpResponse, HttpResponseRedirect

from .forms import UserForm
from .models import Login


def user_login(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = UserForm()
    return render(request, 'index1.html', {'form': form})


# Paginator
def index(request):
    queryset =['a','b','c','d']
    p = Paginator(queryset, 1)
    try:
        p_no = request.GET.get('page')
        p_obj = p.page(p_no)
    except:
        p_obj = p.page(1)
    return render (request,'index1.html',{'p_obj':p_obj})




# If the form value contains more than the '20' letters is throws an error message
def err(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        elif len(q) > 20:
            error = True
        else:
            books = Login.objects.filter(name__icontains=q)
            return render(request, 'index1.html', {'books': books, 'query': q})
    return render(request, 'index1.html', {'error': error})


# @login_required
# def user_login(request):
#     if request.method == "POST":
#         phone = request.POST.get('phone')
#         password = request.POST.get('password')
#         user = authenticate(username=phone, password=password)
#         if user:
#             login(request,user)
#             return HttpResponseRedirect('/users/home')
#         else:
#             error = " Sorry! Phone Number and Password didn't match, Please try again ! "
#             return render(request, 'index1.html',{'error':error})
#     else:
#         return render(request, 'index1.html')


# @login_required
def users_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        pass_1 = request.POST.get('password1')
        pass_2 = request.POST.get('password2')
        if pass_1 == pass_2:
             user = User.objects.create_user(
                                              username=phone,
                                              email=email,
                                              password=pass_1,
                                             )
                                             
                # print '-------'
                # print user
                # print '-------'

             return HttpResponseRedirect("/main")
        else:
             error = " Password Mismatch "
             return render(request, 'signup.html',{"error":error})
    else:
         return render(request, 'signup.html')