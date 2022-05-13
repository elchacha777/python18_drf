from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.decorators import login_required

from api.models import Like, Product, Comment
from api.serializers import ProductSerializer, CommentSerializer

@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['POST'])
def create_product(request):
    product = ProductSerializer(data=request.data)
    
    if Product.objects.filter(**request.data).exists():
        raise serializers.ValidationError('Already Exists')

    if product.is_valid():
        product.save()
        return Response(product.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update_product(request, pk):
    get_object_or_404(Product, id=pk).delete()

    product = ProductSerializer(data=request.data)
    
    if Product.objects.filter(**request.data).exists():
        raise serializers.ValidationError('Already Exists')

    if product.is_valid():
        product.save()
        return Response(product.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    


@api_view(['DELETE'])
def delete_product(request, pk):
    get_object_or_404(Product, id=pk).delete()
    return Response( {'msg': 'Your product deleted'})


"""==========V2==========="""

# ViewSet

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['action'] = self.action
        return context

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


@api_view(['GET'])
@login_required
def toggle_like(request, id):
    product = Product.objects.get(id=id)
    if Like.objects.filter(user=request.user, product=product).exists():
        Like.objects.get(user=request.user, product=product).delete()
    else:
        Like.objects.create(user=request.user, product=product)
    serializer = ProductSerializer(product)
    return Response(serializer.data)
