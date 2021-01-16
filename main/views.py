from django.shortcuts import render, HttpResponse

def homepage(request):
    return render(request, "index.html")

def test(request):
    return render(request, "test.html")

def second(request):
    return HttpResponse("test 2 page")

def third(request):
    return render(request, "test3.html")

def fourth(request):
    return render(request, "text.html")

def fives(request):
    return render(request, "text2.html")