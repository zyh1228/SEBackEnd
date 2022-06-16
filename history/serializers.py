from rest_framework import serializers
from history.models import History
from objModel.serializers import ObjModelSerializer


class HistoryUserSerializers(serializers.ModelSerializer):
    obj_model = ObjModelSerializer()

    class Meta:
        model = History
        fields = ['id', 'view_time', 'created_by', 'obj_model']
