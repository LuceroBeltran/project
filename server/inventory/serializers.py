from rest_framework import serializers
from .models import Product, Category, NFC


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class NFCSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFC
        fields = ('id', 'status', 'created_at')


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    nfc = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'image', 'price', 'description', 'category', 'stock', 'nfc']

    def get_category(self, obj):
        return obj.category.name

    def get_nfc(self, obj):
        return {
            'id': obj.NFC.id if obj.NFC else None,
            'status': obj.NFC.status if obj.NFC else None
        }

    def get_image(self, obj):
        # return obj.image.image.url if obj.image else None <- use optionaly

        request = self.context.get('request')
        return request.build_absolute_uri(obj.image.image.url) if obj.image else None


class ProductCreateUpdateSerializer(serializers.ModelSerializer):
    category_id = serializers.UUIDField(write_only=True)
    nfc_id = serializers.UUIDField(write_only=True, required=False, allow_null=True)

    class Meta:
        model = Product
        fields = ['name', 'image', 'price', 'description', 'category_id', 'stock', 'nfc_id']

    def create(self, validated_data):
        category_id = validated_data.pop('category_id')
        nfc_id = validated_data.pop('nfc_id', None)

        category = Category.objects.get(id=category_id)
        nfc = NFC.objects.get(id=nfc_id) if nfc_id else None

        return Product.objects.create(category=category, NFC=nfc, **validated_data)

    def update(self, instance, validated_data):
        category_id = validated_data.pop('category_id', None)
        nfc_id = validated_data.pop('nfc_id', None)

        if category_id:
            instance.category = Category.objects.get(id=category_id)
        if nfc_id:
            instance.NFC = NFC.objects.get(id=nfc_id)

        instance.name = validated_data.get('name', instance.name)
        instance.image = validated_data.get('image', instance.image)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        return instance
