from django.shortcuts import render

from django.http import HttpResponse

def test(request):
    print("test function is called view")
    return HttpResponse("<h1>Hello shweta Amol loves you</h1>")
