from utils.api.api import APIView, validate_serializer
from account.decorators import login_required, admin_required, ensure_created_by
from objModel.serializers import CreateCategorySerializer, EditCategorySerializer, CategorySerializer
from objModel.models import Category


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

        :param request:
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

    def post(self, request):
        return self.success()

    def get(self, request):
        return self.success()

    def put(self, request):
        return self.success()

    def delete(self, request):
        return self.success()
