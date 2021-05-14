from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from serverAccount.models import Account
from serverAccount.serializers import AccountListSerializer

from common.hasher import AESCipher


class AccountListViewSet(ModelViewSet):

    def list(self, request):
        results = Account.objects.filter(is_active=True)
        for res in results:
            decrypted_id = AESCipher().decrypt_str(res.server_id)
            decrypted_pwd = AESCipher().decrypt_str(res.server_password)
            res.server_id = decrypted_id
            res.server_password = decrypted_pwd

        serializer = AccountListSerializer(results, many=True)
        return Response(serializer.data)

