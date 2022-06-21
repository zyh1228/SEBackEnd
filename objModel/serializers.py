from django import forms
from rest_framework import serializers

from objModel.models import Category, ObjModel
from account.serializers import UserNameSerializer


class CreateOrEditCategorySerializer(serializers.Serializer):
    category_name = serializers.CharField(max_length=32)


class CreateCategorySerializer(CreateOrEditCategorySerializer):
    pass


class EditCategorySerializer(CreateOrEditCategorySerializer):
    id = serializers.IntegerField()


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'category_name']


class CreateOrEditObjModelForm(forms.Form):
    name = forms.CharField(max_length=32)
    description = forms.CharField(max_length=1024)
    category = forms.CharField(max_length=32)
    cover = forms.ImageField()


class UploadObjModelForm(forms.Form):
    id = forms.IntegerField()
    model = forms.FileField()


class CreateObjModelForm(CreateOrEditObjModelForm):
    pass


class EditObjModelForm(CreateOrEditObjModelForm):
    id = forms.IntegerField()


class ObjModelListSerializer(serializers.ModelSerializer):
    created_by = UserNameSerializer()
    category = CategorySerializer()

    class Meta:
        model = ObjModel
        fields = ['id', 'name', 'cover', 'file_type', 'category', 'last_edit_time', 'created_by']


class ObjModelSerializer(serializers.ModelSerializer):
    created_by = UserNameSerializer()
    category = CategorySerializer()

    class Meta:
        model = ObjModel
        fields = ['id', 'name', 'description', 'cover', 'file_type', 'model_file', 'category', 'last_edit_time', 'created_by']
