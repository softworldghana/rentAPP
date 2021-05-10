from django.shortcuts import render


def system_data(request):
    return render(request, "system_data.html")