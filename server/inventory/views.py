from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Product, NFC, Category
from .serializers import ProductCreateUpdateSerializer, ProductSerializer, NFCSerializer, CategorySerializer
from django.shortcuts import get_object_or_404
from rest_framework import status


class IndexApi(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        context = {
            'message': 'server ready'
        }
        return Response(context)


class ProductoView(APIView):
    def get(self, request, product_id=None):
        if product_id:
            product = get_object_or_404(Product, id=product_id)
            serializer = ProductSerializer(product, context={'request': request}) # <- remove context if use aws
            return Response(serializer.data)
        else:
            product = Product.objects.all()
            serializer = ProductSerializer(product, many=True, context={'request': request}) # <- remove context if use aws
            return Response(serializer.data)

    def post(self, request):
        self.check_permissions(request)

        serializer = ProductCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.save()
            return Response(ProductSerializer(product).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, producto_id):
        self.check_permissions(request)

        product = get_object_or_404(Product, id=producto_id)
        serializer = ProductCreateUpdateSerializer(product, data=request.data)
        if serializer.is_valid():
            product = serializer.save()
            return Response(ProductSerializer(product).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, producto_id):
        self.check_permissions(request)

        product = get_object_or_404(Product, id=producto_id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def check_permissions(self, request):
        if request.method == 'POST':
            permission_classes = [IsAuthenticated]
            for permission in permission_classes:
                if not permission().has_permission(request, self):
                    raise NotFound()


class NFCView(APIView):
    def get(self, request, nfc_id=None):
        self.check_permissions(request)

        if nfc_id:
            nfc = get_object_or_404(NFC, id=nfc_id)
            serializer = NFCSerializer(nfc)
            return Response(serializer.data)
        else:
            nfc_list = NFC.objects.all()
            serializer = NFCSerializer(nfc_list, many=True)
            return Response(serializer.data)

    def post(self, request):
        self.check_permissions(request)

        serializer = NFCSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, nfc_id):
        self.check_permissions(request)

        nfc = get_object_or_404(NFC, id=nfc_id)
        serializer = NFCSerializer(nfc, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, nfc_id):
        self.check_permissions(request)

        nfc = get_object_or_404(NFC, id=nfc_id)
        nfc.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def check_permissions(self, request):
            if request.method == 'POST':
                permission_classes = [IsAuthenticated]
                for permission in permission_classes:
                    if not permission().has_permission(request, self):
                        raise NotFound()


class CategoryView(APIView):
    def get(self, request, category_id=None):
        if category_id:
            category = get_object_or_404(Category, id=category_id)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        else:
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
