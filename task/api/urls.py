from rest_framework.routers import DefaultRouter

from .views import TaskModelViewSet

router = DefaultRouter()
router.register('', TaskModelViewSet)
urlpatterns = router.urls
