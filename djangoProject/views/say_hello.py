from django.http import HttpResponse,HttpRequest


def say_hello(request):
    return HttpResponse("Hello World Ritik")

def say_hello_with_name(request:HttpRequest,name):
    # print(request.headers)
    return HttpResponse(f"Hello {name}")
