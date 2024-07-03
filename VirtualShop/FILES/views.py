from django.http import HttpResponse

def home(request):
    return HttpResponse("Pagina de home") # -> Esto debera cambiarse al archivo HTML correspondiente

def buy(request):
    return HttpResponse("Pagina para pagar")

def login(request):
    doc = open("VirtualShop/TEMPLATES/login_page.html")
    return HttpResponse(doc)

def register(request):
    doc = open("VirtualShop/TEMPLATES/register_page.html")