from rest_framework import serializers

from product.models import *


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ('id', 'image',)


class AboutProductSerializers(serializers.ModelSerializer):
    included = serializers.SlugRelatedField(
        slug_field="title", read_only=True
    )
    key_features = serializers.SlugRelatedField(
        slug_field="title", read_only=True
    )

    class Meta:
        model = AboutProduct
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('id', 'name', 'hex')


class ValueCharacterSerializer(serializers.ModelSerializer):
    key_features = serializers.SlugRelatedField(
        slug_field="title", read_only=True
    )

    class Meta:
        model = ValueCharacter
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    category_people = serializers.SlugRelatedField(
        slug_field="title", read_only=True
    )
    equipment_category = serializers.SlugRelatedField(
        slug_field="title", read_only=True
    )
    type_tire = serializers.SlugRelatedField(
        slug_field="title", read_only=True
    )
    guarantee = serializers.SlugRelatedField(
        slug_field="title", read_only=True
    )
    additional_services = serializers.SlugRelatedField(
        slug_field="title", read_only=True
    )
    gift_wrapping = serializers.SlugRelatedField(
        slug_field="title", read_only=True
    )
    for_whom_category = serializers.SlugRelatedField(
        slug_field="title", read_only=True
    )
    technique_category = serializers.SlugRelatedField(
        slug_field="title", read_only=True
    )
    type_category = serializers.SlugRelatedField(
        slug_field="title", read_only=True
    )

    class Meta:
        model = Category
        fields = '__all__'


class DeliveryPaymentSerializer(serializers.ModelSerializer):
    payment = serializers.SlugRelatedField(
        slug_field='title', read_only=True
    )
    delivery = serializers.SlugRelatedField(
        slug_field='title', read_only=True
    )

    class Meta:
        model = DeliveryPayment
        fields = ('id', 'payment', 'delivery')


class WarrantySerializer(serializers.ModelSerializer):
    class Meta:
        model = Warranty
        fields = ('id', 'title', 'description')


class VersionMaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = VersionMax
        fields = ('id', 'title', 'description')


class ProductMediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Media
        fields = ('id', 'image')


class ProductListSerializer(serializers.ModelSerializer):
    status = serializers.SlugRelatedField(
        slug_field='title', read_only=True, many=True
    )
    image = ProductMediaSerializer(many=True)
    character = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'status', 'image', 'character', 'title', 'old_price', 'new_price')

    def get_character(self, obj):
        queryset = obj.character.filter(key_features__in=[3, 4, 6])
        return ValueCharacterSerializer(queryset, many=True).data


class MenuSerializer(serializers.ModelSerializer):
    subItem = serializers.SlugRelatedField(
        slug_field='subItem', read_only=True
    )

    class Meta:
        model = Menu
        fields = ('id', 'title', 'subItem')


class MediaBannerSerializer(serializers.ModelSerializer):

    class Meta:
        model = MediaBanner
        fields = ('id', 'image',)


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ('id', 'title',)


class BannerFilterSerializer(serializers.ModelSerializer):
    image = MediaBannerSerializer(many=True)
    status_category = StatusSerializer()

    class Meta:
        model = Banner
        fields = ('id', 'title', 'image', 'status_category')


class TypeCategorySerializer(serializers.ModelSerializer):
    # min_price = serializers.SerializerMethodField()
    min_price = serializers.IntegerField()

    class Meta:
        model = TypeCategory
        fields = ('id', 'title', 'image', 'min_price')

    # def get_min_price(self, obj):
    #     products = Product.objects.filter(category__tech_category__title=obj.title)
    #     if products.exists():
    #         return products.aggregate(models.Min('new_price'))['new_price__min']
    #     return None


class FormWhomSerializer(serializers.ModelSerializer):

    class Meta:
        model = ForWhomCategory
        fields = ('id', 'title')


class SubItemsSerializer(serializers.ModelSerializer):
    titleType = serializers.SlugRelatedField(
        slug_field='titleType', read_only=True
    )
    subItems = FormWhomSerializer(many=True)

    class Meta:
        model = SubItems
        fields = ('id', 'titleType', 'subItems')


class CatalogCategoryListSerializer(serializers.ModelSerializer):
    title = serializers.SlugRelatedField(
        slug_field='title', read_only=True
    )
    subItems = SubItemsSerializer(many=True)

    class Meta:
        model = CatalogCategory
        fields = ('id', 'title', 'subItems')
