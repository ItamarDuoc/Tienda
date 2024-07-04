from django.http import HttpResponse
from django.template import Template, Context

def buy(request):
    doc = open("VirtualShop/TEMPLATES/buy_page.html")
    plt = Template(doc.read())
    doc.close()
    ctx = Context()
    pagina = plt.render(ctx)
    return HttpResponse(pagina)

def digimon(request):
    doc = open("VirtualShop/TEMPLATES/digimon_page.html")
    plt = Template(doc.read())
    doc.close()
    ctx = Context()
    pagina = plt.render(ctx)
    return HttpResponse(pagina)

def evangelion(request):
    doc = open("VirtualShop/TEMPLATES/evangelion_page.html")
    plt = Template(doc.read())
    doc.close()
    ctx = Context()
    pagina = plt.render(ctx)
    return HttpResponse(pagina)

def home(request):
    doc = open("VirtualShop/TEMPLATES/home_page.html")
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

def pokemon(request):
    doc = open("VirtualShop/TEMPLATES/pokemon_page.html")
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

def simpsons(request):
    doc = open("VirtualShop/TEMPLATES/simpsons_page.html")
    plt = Template(doc.read())
    doc.close()
    ctx = Context()
    pagina = plt.render(ctx)
    return HttpResponse(pagina)