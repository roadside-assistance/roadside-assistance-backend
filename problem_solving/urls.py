from rest_framework.routers import DefaultRouter

from problem_solving.problem.view import ProblemViewSet

router = DefaultRouter()
router.register(r'problems', ProblemViewSet, basename='problem')
urlpatterns = router.urls
