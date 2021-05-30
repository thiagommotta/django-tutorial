from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("Ola. Voce esta na pagina principal do Polls")


