from django.urls import path
from rest_framework import routers

from .views import VoteViewSet

app_name = 'vote'

router = routers.SimpleRouter()
router.register('vote', VoteViewSet, basename='api')

urlpatterns = router.urls
