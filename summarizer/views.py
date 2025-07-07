import json

from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import ChatSummaryRequestSerializer
from .ai_utils import summarize_chat
import logging

logger = logging.getLogger(__name__)


@api_view(['POST'])
@permission_classes([AllowAny])
def summarize_chat_view(request):
    body = json.loads(request.body)
    serializer = ChatSummaryRequestSerializer(data=body)
    if serializer.is_valid():
        chat = serializer.validated_data['chat']
        try:
            logger.info(f"Request: {chat}")
            summary = summarize_chat(chat)
            logger.info(f"Response: {summary}")
            return Response({"summary": summary}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error summarizing chat: {str(e)}")
            return Response({"error": "Failed to summarize chat."}, status=500)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
