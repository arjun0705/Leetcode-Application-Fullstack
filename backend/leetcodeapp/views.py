from django.shortcuts import render,redirect
import sqlite
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response


def home(request):
    return render(request,"index.html")


@api_view(['POST','GET'])
def signup(request):
    if request.data:
        data=(request.data['fullname'],
        request.data['address'],
        request.data['username'],
        request.data['password'])
        sqlite.signup(data)
        return redirect('login')
        # messages.success(request,"Your Account has been successfully Created")
    return render(request,"signup.html")

    # if request.data:
    #     data = sqlite.getuser()
    #     response = []
    #     for d in data:
    #         response.append({'fullname': d[0], 'address': d[1], 'username': d[2], 'password': d[3]})
    #         return JsonResponse(data={'data': response})
    #     sqlite.signup(data)

    # return render(request,"signup.html")
    # # return JsonResponse(data={'data':[]})

@api_view(['POST','GET'])
def problems(request):
    if request.data:
        data=(request.data['title'],
        request.data['description'],
        request.data['solutions'],
        request.data['difficulty'],
        request.data['userid'],
        request.data['acceptence'])
        sqlite.createproblem(data)
    return render(request,'problems.html')
    # return render(request,"signup.html")


    
# @api_view(['POST','GET'])
# def problems(request):
#     response = []
#     if request.data:
#         sqlite.createproblem(request.data)
#         data = sqlite.getproblem()
#         for d in data:
#             response.append({'title': d[0], 'description': d[1], 'solution': d[2], 'difficulty': d[3],'userid': d[4],'acceptence': d[5]})
#             return JsonResponse(data={'data': response})
#     print('>>>>>>>>>>>>>>',response)
#     return JsonResponse(response)

 
@api_view(['POST','GET'])
def login(request):
    
    if request.data:
        data=(request.data['username'],
        request.data['password'])
        sqlite.login(data)
        return redirect('problems')
    return render(request,'login.html')
