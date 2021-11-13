from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from apps.APIs.views import EndpointViewSet
from apps.APIs.views import MLAlgorithmViewSet
from apps.APIs.views import MLAlgorithmStatusViewSet
from apps.APIs.views import MLRequestViewSet
from apps.APIs.views import PredictView 

router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints", EndpointViewSet, basename="endpoints")
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register(r"mlalgorithmstatuses", MLAlgorithmStatusViewSet, basename="mlalgorithmstatuses")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")

urlpatterns = [
    url(r"^api/v1/", include(router.urls)),
    # add predict url
    url(
        r"^api/v1/(?P<endpoint_name>.+)/predict$", PredictView.as_view(), name="predict"),
]