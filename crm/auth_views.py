import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import permissions
from .serializers import LoginSerializer
from django.contrib.auth import authenticate
from .serializers import UserSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer

logger = logging.getLogger(__name__)

class LoginAPIView(APIView):
    permission_classes = []

    def post(self, request):
        # Extract username and password from the request
        username = request.data.get('username')
        password = request.data.get('password')

        # Validate if username and password are provided
        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        # Log the attempt to authenticate
        logger.info("Attempting to authenticate user: %s", username)

        try:
            # Authenticate the user
            user = authenticate(username=username, password=password)

            # Check if the user is None (authentication failed)
            if user is None:
                logger.error("Authentication failed for user: %s", username)
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

            # Ensure the user object is valid and has '_meta' attribute (indicating it's a valid Django model instance)
            if not hasattr(user, '_meta'):
                logger.error("User object is None or invalid for user: %s", username)
                return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            user_data = UserSerializer(user).data

            # Return response with tokens and user data
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': user_data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            # Catch any unexpected errors during the process
            logger.error("Error generating tokens for user: %s - %s", username, str(e))
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)