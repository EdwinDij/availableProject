
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .serializers import ShopSerializer

from .models import Shop

@api_view(['POST'])
def register_shop(request):
    serializer = ShopSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        shop_name = serializer.validated_data['shop_name']
        password = serializer.validated_data['password']
        
        # Check if email already exists
        if Shop.objects.filter(email=email).exists():
            return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Check if shop name already exists
        if Shop.objects.filter(shop_name=shop_name).exists():
            return Response({'error': 'Shop name already exists'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Hash the password
        hashed_password = make_password(password)
        
        # Create a new shop
        shop = Shop(email=email, shop_name=shop_name, password=hashed_password)
        shop.save()
        
        return Response({'message': 'Shop registered successfully'}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
