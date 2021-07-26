from django.urls import include, path

from problem_solving.problem.view import IssueProblemView, GetAssignedProblems, ConfirmProblem, GetAssignedMission
from django.contrib import admin

urlpatterns = [
    # path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('problem_solving/issue-problem/', IssueProblemView.as_view(), name='issue-problem'),
    path('problem_solving/get-assigned-problems/', GetAssignedProblems.as_view(), name='get-assigned-problems'),
    path('problem_solving/confirm-problem/', ConfirmProblem.as_view(), name='confirm-problem'),
    path('problem_solving/get-assigned-mission/', GetAssignedMission.as_view(), name='get-assigned-mission'),

    path('chat/', include('chat.urls')),
    path('problem-solving/', include('problem_solving.urls')),
]
