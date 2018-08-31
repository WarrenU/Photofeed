from django.conf.urls import url, include

from rest_framework import routers

from photos.views import PhotosViewSet
from photographers.views import PhotographersViewSet

router = routers.DefaultRouter()
router.register('photos', PhotosViewSet)
router.register('photographers', PhotographersViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework'))
]