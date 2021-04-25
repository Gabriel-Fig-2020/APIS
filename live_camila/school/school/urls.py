
from django.contrib import admin
from django.urls import path, include
from grades.views import GradeViewSet
from rest_framework.routers import DefaultRouter
from rest_framework import routers

router = DefaultRouter()
router.register(r'grades', GradeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('grades/', grades, name='grades'),
]
