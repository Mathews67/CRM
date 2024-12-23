from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from rest_framework import viewsets
from .models import CrimeCategory, Crime, Officer, ReportingOfficer, CourtCase, Witness, PoliceStation, Complaint
from .forms import CrimeForm, OfficerForm, ReportingOfficerForm, CourtCaseForm, WitnessForm, PoliceStationForm, ComplaintForm
from .serializers import CrimeCategorySerializer, CrimeSerializer, OfficerSerializer, ReportingOfficerSerializer, CourtCaseSerializer, WitnessSerializer, PoliceStationSerializer, ComplaintSerializer
from .auth_views import LoginAPIView 

# Regular Views for Crime Categories

class CrimeCategoryListView(View):
    def get(self, request):
        crime_categories = CrimeCategory.objects.all()
        return render(request, 'crime_category_list.html', {'crime_categories': crime_categories})

class CrimeCategoryDetailView(View):
    def get(self, request, pk):
        crime_category = get_object_or_404(CrimeCategory, pk=pk)
        return render(request, 'crime_category_detail.html', {'crime_category': crime_category})


# Regular Views for Crimes

class CrimeListView(View):
    def get(self, request):
        crimes = Crime.objects.all()
        return render(request, 'crime_list.html', {'crimes': crimes})

class CrimeDetailView(View):
    def get(self, request, pk):
        crime = get_object_or_404(Crime, pk=pk)
        return render(request, 'crime_detail.html', {'crime': crime})

class CrimeCreateView(View):
    def get(self, request):
        form = CrimeForm()
        return render(request, 'crime_create.html', {'form': form})

    def post(self, request):
        form = CrimeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crime-list')
        return render(request, 'crime_create.html', {'form': form})


# Regular Views for Officers

class OfficerListView(View):
    def get(self, request):
        officers = Officer.objects.all()
        return render(request, 'officer_list.html', {'officers': officers})

class OfficerDetailView(View):
    def get(self, request, pk):
        officer = get_object_or_404(Officer, pk=pk)
        return render(request, 'officer_detail.html', {'officer': officer})

class OfficerCreateView(View):
    def get(self, request):
        form = OfficerForm()
        return render(request, 'officer_create.html', {'form': form})

    def post(self, request):
        form = OfficerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('officer-list')
        return render(request, 'officer_create.html', {'form': form})


# Regular Views for Reporting Officers

class ReportingOfficerListView(View):
    def get(self, request):
        reporting_officers = ReportingOfficer.objects.all()
        return render(request, 'reporting_officer_list.html', {'reporting_officers': reporting_officers})

class ReportingOfficerDetailView(View):
    def get(self, request, pk):
        reporting_officer = get_object_or_404(ReportingOfficer, pk=pk)
        return render(request, 'reporting_officer_detail.html', {'reporting_officer': reporting_officer})

class ReportingOfficerCreateView(View):
    def get(self, request):
        form = ReportingOfficerForm()
        return render(request, 'reporting_officer_create.html', {'form': form})

    def post(self, request):
        form = ReportingOfficerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reporting-officer-list')
        return render(request, 'reporting_officer_create.html', {'form': form})


# Regular Views for Court Cases

class CourtCaseListView(View):
    def get(self, request):
        court_cases = CourtCase.objects.all()
        return render(request, 'court_case_list.html', {'court_cases': court_cases})

class CourtCaseDetailView(View):
    def get(self, request, pk):
        court_case = get_object_or_404(CourtCase, pk=pk)
        return render(request, 'court_case_detail.html', {'court_case': court_case})

class CourtCaseCreateView(View):
    def get(self, request):
        form = CourtCaseForm()
        return render(request, 'court_case_create.html', {'form': form})

    def post(self, request):
        form = CourtCaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('court-case-list')
        return render(request, 'court_case_create.html', {'form': form})


# Regular Views for Witnesses

class WitnessListView(View):
    def get(self, request):
        witnesses = Witness.objects.all()
        return render(request, 'witness_list.html', {'witnesses': witnesses})

class WitnessDetailView(View):
    def get(self, request, pk):
        witness = get_object_or_404(Witness, pk=pk)
        return render(request, 'witness_detail.html', {'witness': witness})

class WitnessCreateView(View):
    def get(self, request):
        form = WitnessForm()
        return render(request, 'witness_create.html', {'form': form})

    def post(self, request):
        form = WitnessForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('witness-list')
        return render(request, 'witness_create.html', {'form': form})


# Regular Views for Police Stations

class PoliceStationListView(View):
    def get(self, request):
        police_stations = PoliceStation.objects.all()
        return render(request, 'police_station_list.html', {'police_stations': police_stations})

class PoliceStationDetailView(View):
    def get(self, request, pk):
        police_station = get_object_or_404(PoliceStation, pk=pk)
        return render(request, 'police_station_detail.html', {'police_station': police_station})

class PoliceStationCreateView(View):
    def get(self, request):
        form = PoliceStationForm()
        return render(request, 'police_station_create.html', {'form': form})

    def post(self, request):
        form = PoliceStationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('police-station-list')
        return render(request, 'police_station_create.html', {'form': form})


# Regular Views for Complaints

class ComplaintListView(View):
    def get(self, request):
        complaints = Complaint.objects.all()
        return render(request, 'complaint_list.html', {'complaints': complaints})

class ComplaintDetailView(View):
    def get(self, request, pk):
        complaint = get_object_or_404(Complaint, pk=pk)
        return render(request, 'complaint_detail.html', {'complaint': complaint})

class ComplaintCreateView(View):
    def get(self, request):
        form = ComplaintForm()
        return render(request, 'complaint_create.html', {'form': form})

    def post(self, request):
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('complaint-list')
        return render(request, 'complaint_create.html', {'form': form})

# API View for Officer ViewSet
class OfficerViewSet(viewsets.ModelViewSet):
    queryset = Officer.objects.all()
    serializer_class = OfficerSerializer

class CrimeCategoryViewSet(viewsets.ModelViewSet):
    queryset = CrimeCategory.objects.all()
    serializer_class = CrimeCategorySerializer

class CrimeViewSet(viewsets.ModelViewSet):
    queryset = Crime.objects.all()
    serializer_class = CrimeSerializer

class OfficerViewSet(viewsets.ModelViewSet):
    queryset = Officer.objects.all()
    serializer_class = OfficerSerializer

class ReportingOfficerViewSet(viewsets.ModelViewSet):
    queryset = ReportingOfficer.objects.all()
    serializer_class = ReportingOfficerSerializer

class CourtCaseViewSet(viewsets.ModelViewSet):
    queryset = CourtCase.objects.all()
    serializer_class = CourtCaseSerializer

class WitnessViewSet(viewsets.ModelViewSet):
    queryset = Witness.objects.all()
    serializer_class = WitnessSerializer

class PoliceStationViewSet(viewsets.ModelViewSet):
    queryset = PoliceStation.objects.all()
    serializer_class = PoliceStationSerializer

class ComplaintViewSet(viewsets.ModelViewSet):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
