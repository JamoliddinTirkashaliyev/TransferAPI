from django.contrib import admin
from django.urls import path, include
from mainApp.views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("culublar", ClubModelViewSet)
router.register("davlatlar", DavlatModelViewSet)
router.register("playerlar", PlayerModelViewSet)
router.register("transferlar", TransferModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
