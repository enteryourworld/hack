from rest_framework import serializers

class TokenRequestSerializer(serializers.Serializer):
    client_id = serializers.CharField(required=True)
    client_secret = serializers.CharField(required=True)
    scope = serializers.ChoiceField(
        choices=['GIGACHAT_API_PERS', 'GIGACHAT_API_B2B', 'GIGACHAT_API_CORP'],
        default='GIGACHAT_API_PERS'
    )

class MessageSerializer(serializers.Serializer):
    role = serializers.ChoiceField(choices=['system', 'user', 'assistant', 'function'])
    content = serializers.CharField()
    attachments = serializers.ListField(child=serializers.CharField(), required=False)

class ChatCompletionSerializer(serializers.Serializer):
    model = serializers.ChoiceField(
        choices=['GigaChat', 'GigaChat-Pro', 'GigaChat-Max'],
        default='GigaChat'
    )
    messages = serializers.ListField(child=MessageSerializer())
    temperature = serializers.FloatField(required=False, min_value=0)
    top_p = serializers.FloatField(required=False, min_value=0, max_value=1)
    stream = serializers.BooleanField(default=False)
    max_tokens = serializers.IntegerField(required=False, min_value=1)
    attachments = serializers.ListField(child=serializers.CharField(), required=False)