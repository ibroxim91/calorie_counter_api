import random
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import login,authenticate

def generate_code() -> str:
    code = ''
    for i in range(6):
        code +=  str(random.randint(0,9) )
    return code    


class RegisterView(APIView):

    def post(self,request):
        username = request.data.get("username")
        password = request.data.get("password")
        phone = request.data.get("phone")
        response = {"status":None, "detail":None}
        if username and not  User.objects.filter(username=username).exists():
            if not  User.objects.filter(phone=phone).exists():

                user = User.objects.create_user(username=username,phone=phone,
                                            verification_code=generate_code(),
                                                    password=password,is_active=False)
                token = Token.objects.create(user=user)
                login(request, user)
                print(token.key)
                response['status'] = "ok"
                response['detail'] = "User created"
                response['token'] =  token.key
                return Response(response)
        response['status'] = "error"
        response['detail'] = "User not created"    
        return Response(response)
                

class VerificationView(APIView):
    # permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self,request):
        print(request.user)
        token = request.data.get("token")
        verification = request.data.get("verification")
        if Token.objects.filter(key=token).count() == 1:
            user = Token.objects.get(key=token).user
            if user.verification_code == verification:
                user.is_active = True
                user.save()
                return Response({"status":"ok","detail":"Verificated"})
        return Response({"status":"error" ,"detail":"Not Verificated"})


def error_404(request, exception):
   context = {}
   return render(request,'admin/404.html', context)
        