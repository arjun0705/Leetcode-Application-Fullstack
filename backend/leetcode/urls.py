from django.urls import path
from leetcode import views

urlpatterns = [
 
    path("signup",views.signup),
    path("login",views.login),
    path("addproblem",views.addProblem),
    path("problem/<int:id>",views.getProblem),
    path("allproblems",views.getProblems),
    path("updateproblem/<int:id>",views.updateProblem),
    path("deleteproblem/<int:id>",views.deleteProblem)
]