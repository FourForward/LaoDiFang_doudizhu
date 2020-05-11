from django.shortcuts import render


def main(request):
    return render(request,'home_page.html')


def login(request):
    return render(request,'login.html')


def b_or_c(request):
    return render(request,'begin_or_continue.html')


def begin(request):
    return render(request,'begin.html')


def continues(request):
    return render(request,'continue.html')


def login_verify(request):
    return None