import random
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User


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
        if not  User.objects.filter(username=username).exists():
            if not  User.objects.filter(phone=phone).exists():

                user = User.objects.create_user(username=username,phone=phone,
                                            verification_code=generate_code(),
                                                    password=password,is_active=False)
                response['status'] = "ok"
                response['detail'] = "User created"
                return Response(response)
        response['status'] = "error"
        response['detail'] = "User not created"    
        return Response(response)
                


def error_404(request, exception):
   context = {}
   return render(request,'admin/404.html', context)
        