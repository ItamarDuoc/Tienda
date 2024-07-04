from django.http import HttpResponse

def home(request):
    return HttpResponse("VirtualShop\FILES\TEMPLATES\home_page.html") # -> Esto debera cambiarse al archivo HTML correspondiente

def buy(request):
    return HttpResponse("Pagina para pagar")

def login(request):
    doc = open("VirtualShop/TEMPLATES/login_page.html")
    return HttpResponse(doc)

def register(request):
    doc = open("VirtualShop/TEMPLATES/register_page.html")