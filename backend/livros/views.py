from django.http import JsonResponse
from .models import Livro
import json


def listar_livros(request):

    if request.method == 'GET':
        livros = list(Livro.objects.values())
        return JsonResponse(livros, safe=False)


def criar_livro(request):

    if request.method == 'POST':

        data = json.loads(request.body)

        livro = Livro.objects.create(
            titulo=data['titulo'],
            autor=data['autor'],
            categoria=data['categoria'],
            ano_publicacao=data['ano_publicacao'],
            disponivel=data.get('disponivel', True)
        )

        return JsonResponse({
            'id': livro.id,
            'titulo': livro.titulo
        }, status=201)


def buscar_livro(request, id):

    try:

        livro = Livro.objects.get(id=id)

        return JsonResponse({
            'id': livro.id,
            'titulo': livro.titulo,
            'autor': livro.autor,
            'categoria': livro.categoria,
            'ano_publicacao': livro.ano_publicacao,
            'disponivel': livro.disponivel
        })

    except Livro.DoesNotExist:
        return JsonResponse(
            {'erro': 'Livro não encontrado'},
            status=404
        )


def atualizar_livro(request, id):

    try:

        livro = Livro.objects.get(id=id)

        data = json.loads(request.body)

        livro.titulo = data['titulo']
        livro.autor = data['autor']
        livro.categoria = data['categoria']
        livro.ano_publicacao = data['ano_publicacao']
        livro.disponivel = data['disponivel']

        livro.save()

        return JsonResponse({
            'mensagem': 'Livro atualizado'
        })

    except Livro.DoesNotExist:
        return JsonResponse(
            {'erro': 'Livro não encontrado'},
            status=404
        )


def deletar_livro(request, id):

    try:

        livro = Livro.objects.get(id=id)

        livro.delete()

        return JsonResponse({
            'mensagem': 'Livro removido'
        })

    except Livro.DoesNotExist:
        return JsonResponse(
            {'erro': 'Livro não encontrado'},
            status=404
        )