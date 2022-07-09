from django.urls import path
from rest_framework import routers

from .views import VoteViewSet

router = routers.SimpleRouter()
router.register('vote', VoteViewSet)

urlpatterns = router.urls