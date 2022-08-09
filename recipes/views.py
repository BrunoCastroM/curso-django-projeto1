from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Bruno Castro de Moura'})  # Aqui não precisa passar o caminho da pasta "templates" o django já sabe a pasta, pois na pasta "settings" já vem configurado a parte do templates, que ele vai chamar o arquivo, então só precisa colocar caminho dentro da pasta templates

    # OBS: Para resolver o problema "TemplateDoesNotExist at" na página é necessário ir no arquivo "settings" da pasta que você startou o projeto (nesse caso "projeto") e ir na parte de "INSTALLED_APPS" e adicionar o app que a gente startou (nesse caso "recipes")
