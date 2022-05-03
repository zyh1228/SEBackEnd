from django.urls import path

from objModel.views import CategoryAPI, ObjModelAPI


urlpatterns = [
    path('category', CategoryAPI.as_view(), name='category_api'),
    path('obj', ObjModelAPI.as_view(), name='obj_model_api'),
]
