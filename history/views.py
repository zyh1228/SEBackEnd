from utils.api.api import APIView, validate_serializer, APIError
from account.decorators import login_required, ensure_created_by
from history.models import History
from history.serializers import HistoryUserSerializers


class HistoryAPI(APIView):

    @login_required
    def get(self, request):
        user = request.user
        histories = History.objects.filter(created_by=user)
        return self.success(self.paginate_data(request, histories, HistoryUserSerializers))

    @login_required
    def delete(self, request):
        history_id = request.GET.get('id')
        user = request.user
        if not history_id:
            return self.error('id is needed')
        try:
            history = History.objects.get(id=history_id)
            ensure_created_by(history, user)
        except History.DoesNotExist:
            return self.error('History does not exist')

        history.delete()

        return self.success()
