from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router for the API views
router = DefaultRouter()
router.register(r'officer-viewset', views.OfficerViewSet, basename='officer-viewset')

urlpatterns = [
    # Crime Category URLs (Class-Based Views)
    path('crime-categories/', views.CrimeCategoryListView.as_view(), name='crime-category-list'),
    path('crime-categories/<int:pk>/', views.CrimeCategoryDetailView.as_view(), name='crime-category-detail'),

    # Crime URLs (Class-Based Views)
    path('crimes/', views.CrimeListView.as_view(), name='crime-list'),
    path('crimes/<int:pk>/', views.CrimeDetailView.as_view(), name='crime-detail'),
    path('crimes/create/', views.CrimeCreateView.as_view(), name='crime-create'),

    # Officer URLs (Class-Based Views)
    path('officers/', views.OfficerListView.as_view(), name='officer-list'),
    path('officers/<int:pk>/', views.OfficerDetailView.as_view(), name='officer-detail'),
    path('officers/create/', views.OfficerCreateView.as_view(), name='officer-create'),

    # Reporting Officer URLs (Class-Based Views)
    path('reporting-officers/', views.ReportingOfficerListView.as_view(), name='reporting-officer-list'),
    path('reporting-officers/<int:pk>/', views.ReportingOfficerDetailView.as_view(), name='reporting-officer-detail'),
    path('reporting-officers/create/', views.ReportingOfficerCreateView.as_view(), name='reporting-officer-create'),

    # Court Case URLs (Class-Based Views)
    path('court-cases/', views.CourtCaseListView.as_view(), name='court-case-list'),
    path('court-cases/<int:pk>/', views.CourtCaseDetailView.as_view(), name='court-case-detail'),
    path('court-cases/create/', views.CourtCaseCreateView.as_view(), name='court-case-create'),

    # Witness URLs (Class-Based Views)
    path('witnesses/', views.WitnessListView.as_view(), name='witness-list'),
    path('witnesses/<int:pk>/', views.WitnessDetailView.as_view(), name='witness-detail'),
    path('witnesses/create/', views.WitnessCreateView.as_view(), name='witness-create'),

    # Police Station URLs (Class-Based Views)
    path('police-stations/', views.PoliceStationListView.as_view(), name='police-station-list'),
    path('police-stations/<int:pk>/', views.PoliceStationDetailView.as_view(), name='police-station-detail'),
    path('police-stations/create/', views.PoliceStationCreateView.as_view(), name='police-station-create'),

    # Complaint URLs (Class-Based Views)
    path('complaints/', views.ComplaintListView.as_view(), name='complaint-list'),
    path('complaints/<int:pk>/', views.ComplaintDetailView.as_view(), name='complaint-detail'),
    path('complaints/create/', views.ComplaintCreateView.as_view(), name='complaint-create'),

    # Include router URLs for OfficerViewSet
    path('api/', include(router.urls)),
]