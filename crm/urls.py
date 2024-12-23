from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .auth_views import LoginAPIView

# Initialize the router
router = DefaultRouter()

# Register all ViewSets with the router
router.register(r'crime-categories', views.CrimeCategoryViewSet)
router.register(r'crimes', views.CrimeViewSet)
router.register(r'officers', views.OfficerViewSet)
router.register(r'reporting-officers', views.ReportingOfficerViewSet)
router.register(r'court-cases', views.CourtCaseViewSet)
router.register(r'witnesses', views.WitnessViewSet)
router.register(r'police-stations', views.PoliceStationViewSet)
router.register(r'complaints', views.ComplaintViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('login/', LoginAPIView.as_view(), name='login'),
]