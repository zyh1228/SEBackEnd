from django.urls import path

from objModel.views import CategoryAPI, ObjModelAPI, UploadObjModelAPI


urlpatterns = [
    path('category', CategoryAPI.as_view(), name='category_api'),
    path('obj', ObjModelAPI.as_view(), name='obj_model_api'),
    path('obj/uploadModel', UploadObjModelAPI.as_view(), name='obj_model_upload_api'),
]
