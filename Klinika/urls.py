from django.contrib import admin
from django.urls import path,include
from app1.views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("bemorlar",BemorModelViewSet)
router.register("joylashtirishlar",JoylashtirishModelViewSet)
from drf_spectacular.views import SpectacularAPIView, \
    SpectacularRedocView, \
    SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apiview_docs/', SpectacularAPIView.as_view(), name="schema"),
    path('docs/', SpectacularSwaggerView.as_view(url_name="schema")),
    path('', include(router.urls)),
    path('xonalar/', XonalarAPIView.as_view()),
    path('bosh_xonalar/', BoshXonalarAPIView.as_view()),
    path('tolovlar/', TolovlarAPIView.as_view()),
    path('bemor/<int:pk>/tolovlar/', BemorTolovlarAPIView.as_view()),
    path('qarzdorliklar/', TolanmaganTolovlarAPIView.as_view()),
]
