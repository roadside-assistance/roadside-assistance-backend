from rest_framework.routers import DefaultRouter

from human_resources.citizen.view import CitizenViewSet

router = DefaultRouter()
router.register(r'citizen', CitizenViewSet, basename='citizen')
urlpatterns = router.urls
