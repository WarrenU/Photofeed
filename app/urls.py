from django.conf.urls import url, include

from rest_framework import routers

from photos import views as photo_views
from photographers import views as photographers_views

router = routers.DefaultRouter()
router.register('photos', photo_views.PhotosViewSet)
router.register('photographers', photographers_views.PhotographersViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework'))
]