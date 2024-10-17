from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Licao
from .serializers import LicaoSerializer

@api_view(['POST'])
def criar_licao(request):
    serializer = LicaoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listar_licoes(request):
    licoes = Licao.objects.all()
    serializer = LicaoSerializer(licoes, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def editar_html_licao(request, id):
    licao = get_object_or_404(Licao, id=id)
    conteudo_html = request.data.get('conteudo_html')
    if conteudo_html:
        licao.conteudo_html = conteudo_html
        licao.save()
        return Response({"message": "Conteúdo HTML atualizado com sucesso"}, status=status.HTTP_200_OK)
    return Response({"error": "Conteúdo HTML inválido"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deletar_licao(request, id):
    licao = get_object_or_404(Licao, id=id)
    licao.delete()
    return Response({"message": "Lição deletada com sucesso"}, status=status.HTTP_204_NO_CONTENT)
