from rest_framework.routers import DefaultRouter

from machine_resources.machine.view import MachineViewSet

router = DefaultRouter()
router.register(r'machines', MachineViewSet, basename='machine')
urlpatterns = router.urls
