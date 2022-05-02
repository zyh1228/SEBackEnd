from rest_framework import serializers
from objModel.models import Category


class CreateOrEditCategorySerializer(serializers.Serializer):
    category_name = serializers.CharField(max_length=1024)


class CreateCategorySerializer(CreateOrEditCategorySerializer):
    pass


class EditCategorySerializer(CreateOrEditCategorySerializer):
    id = serializers.IntegerField()


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'category_name']
