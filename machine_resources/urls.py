from rest_framework.routers import DefaultRouter

from problem_solving.problem.view import ProblemViewSet
from problem_solving.skill.view import SkillViewSet

router = DefaultRouter()
router.register(r'machines', ProblemViewSet, basename='machine')
urlpatterns = router.urls
