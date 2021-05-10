from django.shortcuts import HttpResponse


def properties(request):
    return HttpResponse(request, "Properties")