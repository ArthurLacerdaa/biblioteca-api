from django.http import JsonResponse
from .models import Usuario
import json


def listar_usuarios(request):

    if request.method == 'GET':
        usuarios = list(Usuario.objects.values())
        return JsonResponse(usuarios, safe=False)


def criar_usuario(request):

    if request.method == 'POST':

        data = json.loads(request.body)

        usuario = Usuario.objects.create(
            nome=data['nome'],
            email=data['email'],
            senha=data['senha']
        )

        return JsonResponse({
            'id': usuario.id,
            'nome': usuario.nome
        }, status=201)


def buscar_usuario(request, id):

    try:
        usuario = Usuario.objects.get(id=id)

        return JsonResponse({
            'id': usuario.id,
            'nome': usuario.nome,
            'email': usuario.email
        })

    except Usuario.DoesNotExist:
        return JsonResponse({'erro': 'Usuário não encontrado'}, status=404)


def atualizar_usuario(request, id):

    try:
        usuario = Usuario.objects.get(id=id)
        data = json.loads(request.body)

        usuario.nome = data['nome']
        usuario.email = data['email']
        usuario.senha = data['senha']
        usuario.save()

        return JsonResponse({'mensagem': 'Usuário atualizado'})

    except Usuario.DoesNotExist:
        return JsonResponse({'erro': 'Usuário não encontrado'}, status=404)


def deletar_usuario(request, id):

    try:
        usuario = Usuario.objects.get(id=id)
        usuario.delete()

        return JsonResponse({'mensagem': 'Usuário removido'})

    except Usuario.DoesNotExist:
        return JsonResponse({'erro': 'Usuário não encontrado'}, status=404)