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
                return JsonResponse(data={"fname":user[0], "lname":user[1],"email":[2]})
            return JsonResponse(data={"msg":"wrong password.."})
        return JsonResponse(data={"msg":"wrong email"}) 
    return JsonResponse("wrong request")          

@csrf_exempt
def addProblem(request):
    if request.method == "POST":
        problemTitle = json.loads(request.body)["title"]
        problemDescription = json.loads(request.body)["description"]
        problemDifficulty = json.loads(request.body)['difficulty']
        problemSolution = json.loads(request.body)["solution"]
        usrid = json.loads(request.body)["userId"]
        sqlite.addProblem((problemTitle,problemDescription,problemDifficulty,problemSolution,usrid))
        return JsonResponse(data={"msg":"problem added successfully..!!"})
    return JsonResponse(data={"msg":"wrong request"})

@csrf_exempt
def getProblem(request,id):
    if request.method == "GET":
        problem = sqlite.getProblem(id)
        return JsonResponse(data = {"msg":problem})

@csrf_exempt
def getProblems(request):
    if request.method == "GET":
        problems = sqlite.getProblems()
        print(problems)
        return JsonResponse(data = {"msg":problems})

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

@csrf_exempt
def deleteProblem(request,id):
    if request.method == "DELETE":
        sqlite.deleteProblem(id)
        return JsonResponse(data={"msg":"problem deleted successfully...!!"})
        
