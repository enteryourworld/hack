from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import uuid
import base64
from .serializers import TokenRequestSerializer, ChatCompletionSerializer

class GetTokenView(APIView):
    def post(self, request):
        serializer = TokenRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        client_id = serializer.validated_data['client_id']
        client_secret = serializer.validated_data['client_secret']
        scope = serializer.validated_data.get('scope', 'GIGACHAT_API_PERS')
        
        auth_string = f"{client_id}:{client_secret}"
        base64_auth = base64.b64encode(auth_string.encode()).decode()
        
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'RqUID': str(uuid.uuid4()),
            'Authorization': f'Basic {base64_auth}'
        }
        
        try:
            response = requests.post(
                'https://ngw.devices.sberbank.ru:9443/api/v2/oauth',
                headers=headers,
                data={'scope': scope},
                verify=False  # Для тестов, в продакшене нужен правильный SSL
            )
            return Response(response.json(), status=response.status_code)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ChatCompletionView(APIView):
    def post(self, request):
        serializer = ChatCompletionSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        token = request.auth  # Если используете DRF authentication
        
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {token}',
            'X-Request-ID': str(uuid.uuid4()),
            'X-Session-ID': str(uuid.uuid4())
        }
        
        try:
            response = requests.post(
                'https://gigachat.devices.sberbank.ru/api/v1/chat/completions',
                headers=headers,
                json=serializer.validated_data
            )
            return Response(response.json(), status=response.status_code)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)