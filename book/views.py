
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book
from .forms import BookForm, UserLoginForm, UserRegisterForm
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    get_user_model,
)


# Create your views here.


def home(request):
    #return HttpResponse("<h1>In the home view</h1>")
    return render(request, 'base.html', {})

def book_list(request):
    qs = Book.objects.all()
    context = {
        "book_list" : qs
    }
    template = "book_list.html"
    return render(request, template, context)

def book_detail(request, id=None):
    qs = Book.objects.get(id=id)
    context = {
        "book": qs
    }
    template = "book_detail.html"
    return render(request, template, context)


def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect("/book/list")
    context = {
            'form': form  #use "BookForm" or "BookForm()" to remain on same page with empty form
        }
    template = "book_create.html"
    return render(request, template, context)

def book_update(request, id=None):
    obj = Book.objects.get(id=id)
    form = BookForm(request.POST or None, instance=obj)
    context = {
        "obj": obj,
        "form": form,
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect("/book/{num}".format(num=obj.id))
    template = "book_update.html"
    return render(request, template, context)


def book_delete(request, id=None):
    form = get_object_or_404(Book, id=id)
    if request.method == "POST":
        form.delete()
        return HttpResponseRedirect("/book/list")
    context = {
        "form": form
    }
    template = "book_delete.html"
    return render(request, template, context)




def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    title = "Register"
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)

        if next:
            return redirect(next)

        return redirect('/book/list')
    context = {
        'form': form,
        'title': title
    }
    # return render(request, "register.html", context)
    return render(request, "form.html", context)


def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    title = "Login"
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)

        if next:
            return redirect(next)

        return redirect('/book/list')
    context = {
        'form': form,
        'title': title
    }
    #return render(request, "login.html", {'form': form,})
    return render(request, "form.html", context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/book")


