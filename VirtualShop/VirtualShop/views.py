from django.http import HttpResponse

def home(request):
    return HttpResponse("Pagina de home") # -> Esto debera cambiarse al archivo HTML correspondiente

def buy(request):
    return HttpResponse("Pagina para pagar")

def login(request):
    return HttpResponse("Pagina de login")