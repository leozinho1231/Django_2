from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated


class FilmesAPIView(APIView):

# permission_classes = (IsAuthenticated,)

    def get(self, request, pk=''):
        if pk == '':
            filmes = Filmes.objects.all()
            serializer = FilmesSerializer(filmes, many=True)
            return Response(serializer.data)
        else:
            filmes = Filmes.objects.get(id=pk)
            serializer =FilmesSerializer(filmes)
            return Response(serializer.data)

    def post(self, request):
        serializer = FilmesSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
        #return Response({"id": serializer.data['id']})

    def put(self, request, pk=''):
        filmes = Filmes.objects.get(id=pk)
        serializer =FilmesSerializer(filmes, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
#atualiza os dados

    def delete(self, request, pk=''):        
        filmes = Filmes.objects.get(id=pk)       
        filmes.delete()
        return Response({"msg": "Apagado com sucesso"})


class CategoriaAPIView(APIView):

# permission_classes = (IsAuthenticated,)

    def get(self, request, pk=''):
        if pk == '':
            categoria = Categoria.objects.all()
            serializer =CategoriaSerializer(categoria, many=True)
            return Response(serializer.data)
        else:
            categoria = Categoria.objects.get(id=pk)
            serializer =CategoriaSerializer(categoria)
            return Response(serializer.data)

    def post(self, request):
        serializer =CategoriaSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response({"msg": "Inserido com sucesso"})
        #return Response({"id": serializer.data['id']})

    def put(self, request, pk=''):
        categoria = Categoria.objects.get(id=pk)
        serializer =CategoriaSerializer(categoria, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
#atualiza os dados

    def delete(self, request, pk=''):        
        categoria = Categoria.objects.get(id=pk)       
        categoria.delete()



class AssinaturaAPIView(APIView):

# permission_classes = (IsAuthenticated,)

    def get(self, request, pk=''):
        if pk == '':
            assinatura = Assinaturas.objects.all()
            serializer = AssinaturaSerializer(assinatura, many=True)
            return Response(serializer.data)
        else:
            assinatura = Assinaturas.objects.get(id=pk)
            serializer = AssinaturaSerializer(assinatura)
            return Response(serializer.data)

    def post(self, request):
        serializer = AssinaturaSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})
        #return Response({"id": serializer.data['id']})

    def put(self, request, pk=''):
        Assinatura = Assinatura.objects.get(id=pk)
        serializer = AssinaturaSerializer(assinatura, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
#atualiza os dados

    def delete(self, request, pk=''):
        assinatura = Assinatura.objects.get(id=pk)
        assinatura.delete()
        return Response({"msg": "Apagado com sucesso"})




class UsuariosAPIView(APIView):

# permission_classes = (IsAuthenticated,)

    def get(self, request, pk=''):
        if pk == '':
            usuarios = Usuario.objects.all()
            serializer =UsuariosSerializer(usuarios, many=True)
            return Response(serializer.data)
        else:
            usuarios = Usuario.objects.get(id=pk)
            serializer =UsuariosSerializer(usuarios)
            return Response(serializer.data)

    def post(self, request):
        serializer = UsuariosSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})
        #return Response({"id": serializer.data['id']})

    def put(self, request, pk=''):
        usuarios = Usuarios.objects.get(id=pk)
        serializer =UsuariosSerializer(usuarios, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
#atualiza os dados

    def delete(self, request, pk=''):
        usuarios = Usuarios.objects.get(id=pk)
        usuarios.delete()
        return Response({"msg": "Apagado com sucesso"})



class FavoritosAPIView(APIView):

# permission_classes = (IsAuthenticated,)

    def get(self, request, pk=''):
        if pk == '':
            favoritos = Favoritos.objects.all()
            serializer =FavoritosSerializer(favoritos, many=True)
            return Response(serializer.data)
        else:
            favoritos = Favoritos.objects.get(id=pk)
            serializer =FavoritosSerializer(favoritos)
            return Response(serializer.data)

    def post(self, request):
        serializer = FavoritosSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})
        #return Response({"id": serializer.data['id']})

    def put(self, request, pk=''):
        favoritos = Favoritos.objects.get(id=pk)
        serializer =FavoritosSerializer(favoritos, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
#atualiza os dados

    def delete(self, request, pk=''):
        favoritos = Favoritos.objects.get(id=pk)
        favoritos.delete()
        return Response({"msg": "Apagado com sucesso"})








