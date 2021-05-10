from django.shortcuts import render


def agents(request):
    return render(request, 'agents.html')
