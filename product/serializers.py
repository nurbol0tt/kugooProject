from rest_framework import serializers

from product.models import *


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ('image',)


class AboutProductSerializers(serializers.ModelSerializer):
    included = serializers.SlugRelatedField(slug_field="title", read_only=True)
    key_features = serializers.SlugRelatedField(slug_field="title", read_only=True)

    class Meta:
        model = AboutProduct
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'name', 'hex']


class ValueCharacterSerializer(serializers.ModelSerializer):
    key_features = serializers.SlugRelatedField(slug_field="title", read_only=True)

    class Meta:
        model = ValueCharacter
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    category_people = serializers.SlugRelatedField(slug_field="title", read_only=True)
    equipment_category = serializers.SlugRelatedField(slug_field="title", read_only=True)
    type_tire = serializers.SlugRelatedField(slug_field="title", read_only=True)
    guarantee = serializers.SlugRelatedField(slug_field="title", read_only=True)
    additional_services = serializers.SlugRelatedField(slug_field="title", read_only=True)
    gift_wrapping = serializers.SlugRelatedField(slug_field="title", read_only=True)
    for_whom_category = serializers.SlugRelatedField(slug_field="title", read_only=True)
    technique_category = serializers.SlugRelatedField(slug_field="title", read_only=True)
    type_category = serializers.SlugRelatedField(slug_field="title", read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class DeliveryPaymentSerializer(serializers.ModelSerializer):
    payment = serializers.SlugRelatedField(slug_field='title', read_only=True)
    delivery = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = DeliveryPayment
        fields = ('payment', 'delivery')


class WarrantySerializer(serializers.ModelSerializer):
    class Meta:
        model = Warranty
        fields = ('title', 'description')


class VersionMaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = VersionMax
        fields = ('title', 'description')


class ProductSerializer(serializers.ModelSerializer):
    image = MediaSerializer()
    about_product = AboutProductSerializers()
    character = ValueCharacterSerializer()
    category = CategorySerializer()
    deliver_payment = DeliveryPaymentSerializer()
    warranty = WarrantySerializer()
    version_max = VersionMaxSerializer()
    color = ColorSerializer()

    class Meta:
        model = Product
        fields = ('title', 'image', 'about_product',
                  'old_price', 'new_price', 'character',
                  'category', 'bought', 'article',
                  'deliver_payment', 'warranty',
                  'version_max', 'in_stock', 'color',
                  'likes', 'views',
                  )


class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = ('title',)


class MediaBannerSerializer(serializers.ModelSerializer):

    class Meta:
        model = MediaBanner
        fields = ('image',)


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ('title',)


class BannerFilterSerializer(serializers.ModelSerializer):
    image = MediaBannerSerializer(many=True)
    status_category = StatusSerializer()

    class Meta:
        model = Banner
        fields = ('title', 'image','status_category')


class TechnicListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TechniqueCategory
        fields = ('title',)


class TypeCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeCategory
        fields = ('title',)


class CartProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('title', 'old_price' , 'new_price')