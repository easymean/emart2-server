from rest_framework import serializers

from serverAccount.models import Account


class AccountListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ["id", "server_name", "server_ip",  "server_id", "server_password"]
