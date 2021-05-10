from django.http import HttpResponse


def tenant_details(request):
    return HttpResponse('Tenants')
