#from .models import User_Details,Answer
#from .serializers import RegistrationSerializer,AnswersSerializer
#from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.serializers import UserRegistrationserializer,Userloginserializer,UserProfileSerializer,UserDetailsSerializer
from account.models import Users,user_details
from django.contrib.auth import authenticate
from reviewiz.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

# Create your views here.
# Function for token generation


# Generate Token Manually
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }
#View for user registration
class UserRegistrationView(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request,format=None):
        serializer=UserRegistrationserializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            User=serializer.save()
            token = get_tokens_for_user(User)
            return Response({'token':token,'message':'Account Creation Successful'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    """
    def get(self,request,format=None):
        All_user=Users.objects.all()
        serial=UserRegistrationserializer(All_user,many=True)
        return JsonResponse(serial.data, safe=False)"""
#View for User Login
class UserLoginView(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request,format=None):
        serializer=Userloginserializer(data=request.data)
        #print(serializer)
        
        if serializer.is_valid(raise_exception=True):
            username=serializer.data.get('email')
            password=serializer.data.get('password')
            user=authenticate(email=username,password=password)
            print(user)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token':token,'message':'Logged in Successfully'},status=status.HTTP_200_OK)
            else:
                return Response({'message':'Email or Password is not valid'},status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    #print(IsAuthenticated)
    def get(self, request, format=None):
        print(request.user)
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

# User Details Form
class UserDetailsFormView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        serializer = UserDetailsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(users=request.user)
            return Response({'message':'Details Added'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#password change


#email_verification

