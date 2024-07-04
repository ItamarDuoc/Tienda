from django.http import HttpResponse
from django.template import Template, Context

def home(request):
    doc = open("VirtualShop/TEMPLATES/home_page.html")
    plt = Template(doc.read())
    doc.close()
    ctx = Context()
    pagina = plt.render(ctx)
    return HttpResponse(pagina) # -> Esto debera cambiarse al archivo HTML correspondiente

def buy(request):
    doc = open("VirtualShop/TEMPLATES/buy_page.html")
    plt = Template(doc.read())
    doc.close()
    ctx = Context()
    pagina = plt.render(ctx)
    return HttpResponse(pagina)

def login(request):
    doc = open("VirtualShop/TEMPLATES/login_page.html")
    plt = Template(doc.read())
    doc.close()
    ctx = Context()
    pagina = plt.render(ctx)
    return HttpResponse(pagina)

def register(request):
    doc = open("VirtualShop/TEMPLATES/register_page.html")
    plt = Template(doc.read())
    doc.close()
    ctx = Context()
    pagina = plt.render(ctx)
    return HttpResponse(pagina)
