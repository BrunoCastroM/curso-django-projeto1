from django.http import HttpResponse

# from django.shortcuts import render


def home(request):
    return HttpResponse('''<!DOCTYPE>
    <html>
    <head><title>Hello world</title></head>
    <body>
        <h1>Hello world!</h1> 
    </body>
    </html>
    ''')


def contato(request):
    return HttpResponse('CONTATO')


def sobre(request):
    return HttpResponse('SOBRE')
