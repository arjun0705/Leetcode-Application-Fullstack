from django.shortcuts import render
import sqlite
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
@csrf_exempt
def signup(request):
    if request.method == "POST":
        fname = json.loads(request.body)["firstName"]
        lname = json.loads(request.body)["lastName"]
        email = json.loads(request.body)["email"]
        password = json.loads(request.body)["password"]
        isAdmin = json.loads(request.body)["isAdmin"]
        sqlite.addUser((fname,lname,email,password,isAdmin))
        return JsonResponse(data={"msg":"user added successfully..!!"})
    # return HttpResponse    


@csrf_exempt
def login(request):
    if request.method == "POST":
        email = json.loads(request.body)["email"]
        password = json.loads(request.body)["password"]
        user = sqlite.checkUser(email)
        if user:
            if user[3] == password:
                request.session["userid"] = user[5]
                return JsonResponse(data={"fname":user[0], "lname":user[1],"email":user[2]})
            return JsonResponse(data={"msg":"wrong password.."})
        return JsonResponse(data={"msg":"wrong email"}) 
    return JsonResponse(data={"msg":"wrong request"})
              

@csrf_exempt
def addProblem(request):
    if request.method == "POST":
        print("**********************",request.session)
        problemTitle = json.loads(request.body)["title"]
        problemDescription = json.loads(request.body)["description"]
        problemDifficulty = json.loads(request.body)['difficulty']
        problemSolution = json.loads(request.body)["solution"]
        # usrid = json.loads(request.body)["userId"]
        sqlite.addProblem((problemTitle,problemDescription,problemDifficulty,problemSolution,1))
        return JsonResponse(data={"msg":"problem added successfully..!!"})
    return JsonResponse(data={"msg":"wrong request"})

@csrf_exempt
def getProblem(request,id):
    if request.method == "GET":
        problem = sqlite.getProblem(id)
        return JsonResponse(data={'title':problem[0],'description':problem[1],'difficulty':problem[2],'solution':problem[3]})
    return JsonResponse(data={"msg":"wrong request"})


@csrf_exempt
def getProblems(request):
    if request.method == "GET":
        problems = sqlite.getProblems()
        data=[]

        for problem in problems:

            data.append({'title':problem[0],'description':problem[1],'difficulty':problem[2],'solution':problem[3]})

        return JsonResponse(data={'data':data})
    return JsonResponse({"msg":"wrong request"})    


@csrf_exempt
def updateProblem(request,id):
    if request.method == "PUT":
        # problem = sqlite.updateProblem()
        problemTitle = json.loads(request.body)["title"]
        problemDescription = json.loads(request.body)["description"]
        problemDifficulty = json.loads(request.body)['difficulty']
        problemSolution = json.loads(request.body)["solution"]    
        sqlite.updateProblem({"title":problemTitle,"description":problemDescription,"difficulty":problemDifficulty,"solution":problemSolution},id)
        return JsonResponse(data={"msg":"record updated successfully..!!"})
    return JsonResponse(data={"msg":"wrong request"})
    
@csrf_exempt
def deleteProblem(request,id):
    if request.method == "DELETE":
        sqlite.deleteProblem(id)
        return JsonResponse(data={"msg":"problem deleted successfully...!!"})
    return JsonResponse(data={"msg":"wrong request"})
        


