import shutil
from os import path
from django.db.models import Q

from utils.api.api import APIView, validate_serializer, APIError
from utils.shortcuts import rand_str
from account.decorators import login_required, admin_required, ensure_created_by
from objModel.serializers import CreateCategorySerializer, EditCategorySerializer, CategorySerializer
from objModel.serializers import CreateObjModelForm, EditObjModelForm, ObjModelSerializer, ObjModelListSerializer
from objModel.models import Category, ObjModel
from history.models import History


class CategoryAPI(APIView):
    """分类API
    """

    @validate_serializer(CreateCategorySerializer)
    @admin_required
    def post(self, request):
        """添加分类

        :param request: 请求
        :return:
        """
        name = request.data.get('category_name')
        user = request.user
        if not user.is_superuser:
            return self.error('permission deny')

        if Category.objects.filter(category_name=name).exists():
            return self.error(f'{name} is already exits')

        Category.objects.create(category_name=name, created_by=user)

        return self.success()

    def get(self, request):
        """查询分类

        :param request: 请求
            keywords:
        :return: 结果
        """
        category = Category.objects

        keyword = request.GET.get("keyword")
        if keyword:
            category = category.filter(name__icontains=keyword)
        return self.success(CategorySerializer(category, many=True).data)

    @validate_serializer(EditCategorySerializer)
    @admin_required
    def put(self, request):
        """修改分类API

        :param request: 请求
        :return:
        """
        category_id = request.data.get('id')
        category_name = request.data.get('category_name')
        user = request.user
        try:
            category = Category.objects.get(id=category_id)
            ensure_created_by(category, user)
        except Category.DoesNotExist:
            return self.error('category does not exist')

        category.category_name = category_name
        category.save()

        return self.success(CategorySerializer(category).data)

    @admin_required
    def delete(self, request):
        """删除分类

        :param request: 请求
            id:
        :return:
        """
        category_id = request.data.get('id')
        user = request.user
        try:
            category = Category.objects.get(id=category_id)
            ensure_created_by(category, user)
        except Category.DoesNotExist:
            return self.error('category does not exist')

        category.delete()

        return self.success()


class ObjModelAPI(APIView):
    """模型API
    """

    def _check_img(self, img):
        if img.size > 2 * 1024 * 1024:
            raise APIError("Picture is too large")

        suffix = path.splitext(img.name)[-1].lower()
        if suffix not in [".gif", ".jpg", ".jpeg", ".bmp", ".png"]:
            raise APIError("Unsupported image format")

        return suffix

    def _check_model(self, model):
        if model.size > 1024 * 1024 * 1024:
            raise APIError("Model is too large")

        suffix = path.splitext(model.name)[-1].lower()
        if suffix not in [".obj", ".glb", ".gltf"]:
            raise APIError("Unsupported model format")

        return suffix

    @login_required
    def post(self, request):
        """添加模型

        :param request: 请求
        :return:
        """
        form = CreateObjModelForm(request.data, request.file)
        if form.is_valid():
            name = form.cleaned_data["name"]
            description = form.cleaned_data["description"]
            category_name = form.cleaned_data["category"]
            cover = form.cleaned_data["cover"]
            model = form.cleaned_data["model"]
        else:
            return self.error("Upload failed")

        image_type = self._check_img(cover)
        file_type = self._check_model(model)

        try:
            category = Category.objects.get(category_name=category_name)
        except Category.DoesNotExist:
            return self.error('Category does not exist')

        cover.name = rand_str(length=16) + image_type
        model.name = rand_str(length=16) + file_type

        obj_model = ObjModel()
        obj_model.file_dir_id = rand_str()
        obj_model.name = name
        obj_model.description = description
        obj_model.category = category
        obj_model.created_by = request.user
        obj_model.cover = cover
        obj_model.model_file = model
        obj_model.file_type = file_type.upper()
        obj_model.save()

        return self.success()

    def get(self, request):
        """查询模型

        :param request: 请求
            id:
            limit:
            offset:
            category:
            type:
            keywords:
        :return:
        """
        model_id = request.GET.get('id')
        if model_id:
            if not request.user.is_authenticated:
                return self.error("Please login first")
            try:
                obj_model = ObjModel.objects.get(id=model_id, visible=True)
            except ObjModel.DoesNotExist:
                return self.error('Model does not exist')
            History.objects.create(created_by=request.user, obj_model=obj_model)
            return self.success(ObjModelSerializer(obj_model).data)

        obj_model = ObjModel.objects.filter(visible=True)

        category = request.GET.get('category')
        if category:
            obj_model = obj_model.filter(category__category_name=category)

        file_type = request.GET.get('type')
        if file_type:
            obj_model = obj_model.filter(file_type=file_type.upper())

        keywords = request.GET.get('keywords')
        if keywords:
            obj_model = obj_model.filter(Q(name__icontains=keywords) | Q(description__icontains=keywords) |
                                         Q(created_by__nick_name__icontains=keywords) |
                                         Q(category__category_name__icontains=keywords))

        return self.success(self.paginate_data(request, obj_model, ObjModelListSerializer))

    # @login_required
    # def put(self, request):
    #     """修改模型
    #
    #     :param request: 请求
    #     :return:
    #     """
    #     print(request.data, request.file)
    #     form = EditObjModelForm(request.data, request.file)
    #     if form.is_valid():
    #         model_id = form.cleaned_data["id"]
    #         name = form.cleaned_data["name"]
    #         description = form.cleaned_data["description"]
    #         category_name = form.cleaned_data["category"]
    #         cover = form.cleaned_data["cover"]
    #         model = form.cleaned_data["model"]
    #     else:
    #         return self.error("Upload failed")
    #
    #     user = request.user
    #
    #     try:
    #         obj_model = ObjModel.objects.get(id=model_id)
    #         ensure_created_by(obj_model, user)
    #     except ObjModel.DoesNotExist:
    #         return self.error('Model dose not exist')
    #
    #     image_type = self._check_img(cover)
    #     file_type = self._check_model(model)
    #
    #     try:
    #         category = Category.objects.get(category_name=category_name)
    #     except Category.DoesNotExist:
    #         return self.error('Category does not exist')
    #
    #     cover.name = rand_str(length=16) + image_type
    #     model.name = rand_str(length=16) + file_type
    #
    #     obj_model = ObjModel()
    #     obj_model.name = name
    #     obj_model.description = description
    #     obj_model.category = category
    #     obj_model.cover.delete()
    #     obj_model.cover = cover
    #     obj_model.model_file.delete()
    #     obj_model.model_file = model
    #     obj_model.file_type = file_type.upper()
    #     obj_model.save()
    #
    #     return self.success(ObjModelSerializer(obj_model).data)

    @login_required
    def delete(self, request):
        """删除模型

        :param request: 请求
            id:
        :return:
        """
        model_id = request.GET.get('id')
        user = request.user
        if not model_id:
            return self.error('id is needed')
        try:
            obj_model = ObjModel.objects.get(id=model_id, visible=True)
            ensure_created_by(obj_model, user)
        except ObjModel.DoesNotExist:
            return self.error('Model does not exist')

        file_dir = obj_model.get_file_dir()
        if path.isdir(file_dir):
            shutil.rmtree(file_dir, ignore_errors=True)

        cover_dir = obj_model.get_cover_dir()
        if path.isdir(cover_dir):
            shutil.rmtree(cover_dir, ignore_errors=True)

        obj_model.delete()

        return self.success()
