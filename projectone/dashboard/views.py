from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    return render (request, 'dashboard/index.html')

def staff (request):
    return render (request, 'dashboard/staff.html')


def inventoryManagement (request):
    return render (request, 'dashboard/inventoryManagement.html')


def userManagement (request):
    return render (request, 'dashboard/userManagement.html')

def myAccount (request):
    return render (request, 'dashboard/myAccount.html')