from rest_framework.routers import DefaultRouter

from human_resources.citizen.view import CitizenViewSet
from human_resources.inspector.view import InspectorViewSet
from human_resources.team.view import TeamViewSet
from human_resources.worker.view import WorkerViewSet

router = DefaultRouter()
router.register(r'citizen', CitizenViewSet, basename='citizen')
router.register(r'inspector', InspectorViewSet, basename='inspector')
router.register(r'worker', WorkerViewSet, basename='worker')
router.register(r'team', TeamViewSet, basename='team')
urlpatterns = router.urls
