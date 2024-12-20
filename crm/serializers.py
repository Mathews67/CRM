from rest_framework import serializers
from .models import (
    CriminalRecord,
    Evidence,
    CrimeCategory,
    ReportingOfficer,
    PoliceStation,
    Complaint,
    Crime,
    Officer,
    CourtCase,
    PoliceStation,
    Complainant,
    Complaint,
    Witness
)
from django.contrib.auth.models import User


# -------------------- Serializers for Models -------------------

# User Serializer for registering users and associating them with ReportingOfficer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


# ReportingOfficer Serializer
class ReportingOfficerSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Nested User serializer for ReportingOfficer

    class Meta:
        model = ReportingOfficer
        fields = ['id', 'user', 'badge_number', 'department', 'phone_number']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        officer = ReportingOfficer.objects.create(user=user, **validated_data)
        return officer


# -------------------- Serializers for CriminalRecord -------------------

class CriminalRecordSerializer(serializers.ModelSerializer):
    crime_category = serializers.StringRelatedField()  # Display category name as string
    reporting_officer = ReportingOfficerSerializer()  # Nested reporting officer data
    evidence = serializers.PrimaryKeyRelatedField(queryset=Evidence.objects.all(), many=True)  # Many to many relationship with Evidence

    class Meta:
        model = CriminalRecord
        fields = ['id', 'criminal_name', 'crime_category', 'crime_date', 'crime_location', 'criminal_status',
                  'description', 'reporting_officer', 'evidence', 'created_at']

    def create(self, validated_data):
        officer_data = validated_data.pop('reporting_officer')
        officer = ReportingOfficer.objects.get(id=officer_data['id'])  # Retrieve officer based on ID
        record = CriminalRecord.objects.create(reporting_officer=officer, **validated_data)
        return record


# -------------------- Serializers for Evidence -------------------

class EvidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evidence
        fields = ['id', 'criminal_record', 'evidence_type', 'evidence_description', 'evidence_file', 'uploaded_at']

    def create(self, validated_data):
        evidence = Evidence.objects.create(**validated_data)
        return evidence


# -------------------- Serializers for CrimeCategory -------------------

class CrimeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CrimeCategory
        fields = ['id', 'category_name', 'category_description']

    def create(self, validated_data):
        category = CrimeCategory.objects.create(**validated_data)
        return category


# -------------------- Serializers for PoliceStation -------------------

class PoliceStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliceStation
        fields = ['id', 'station_name', 'location', 'contact_number']

    def create(self, validated_data):
        station = PoliceStation.objects.create(**validated_data)
        return station


# -------------------- Serializers for Complaint -------------------

class ComplaintSerializer(serializers.ModelSerializer):
    reporting_officer = ReportingOfficerSerializer()  # Nested ReportingOfficer data
    police_station = PoliceStationSerializer()  # Nested PoliceStation data

    class Meta:
        model = Complaint
        fields = ['id', 'complainant_name', 'complaint_details', 'complaint_date', 'status',
                  'reporting_officer', 'police_station']

    def create(self, validated_data):
        officer_data = validated_data.pop('reporting_officer')
        station_data = validated_data.pop('police_station')
        officer = ReportingOfficer.objects.get(id=officer_data['id'])
        station = PoliceStation.objects.get(id=station_data['id'])
        complaint = Complaint.objects.create(reporting_officer=officer, police_station=station, **validated_data)
        return complaint


# -------------------- Serializers for Crime -------------------

class CrimeSerializer(serializers.ModelSerializer):
    crime_category = CrimeCategorySerializer()  # Nested CrimeCategory data
    reporting_officer = ReportingOfficerSerializer()  # Nested ReportingOfficer data

    class Meta:
        model = Crime
        fields = ['id', 'crime_name', 'description', 'crime_date', 'crime_category', 'reporting_officer']

    def create(self, validated_data):
        category_data = validated_data.pop('crime_category')
        officer_data = validated_data.pop('reporting_officer')
        category = CrimeCategory.objects.get(id=category_data['id'])
        officer = ReportingOfficer.objects.get(id=officer_data['id'])
        crime = Crime.objects.create(crime_category=category, reporting_officer=officer, **validated_data)
        return crime


class OfficerSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Nested User serializer for Officer

    class Meta:
        model = Officer
        fields = ['id', 'user', 'badge_number', 'department', 'phone_number']

    def create(self, validated_data):
        # Extract user data and create a user
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        officer = Officer.objects.create(user=user, **validated_data)
        return officer

# -------------------- Serializers for CourtCase -------------------

class CourtCaseSerializer(serializers.ModelSerializer):
    police_station = PoliceStationSerializer()  # Nested PoliceStation data

    class Meta:
        model = CourtCase
        fields = ['id', 'case_number', 'court_name', 'case_status', 'case_details', 'court_date', 'police_station']

    def create(self, validated_data):
        station_data = validated_data.pop('police_station')
        station = PoliceStation.objects.get(id=station_data['id'])
        court_case = CourtCase.objects.create(police_station=station, **validated_data)
        return court_case


# -------------------- Serializers for Complainant -------------------

class ComplainantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complainant
        fields = ['id', 'first_name', 'last_name', 'contact_number', 'email', 'address']

    def create(self, validated_data):
        complainant = Complainant.objects.create(**validated_data)
        return complainant


# serializers.py

class WitnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Witness  # Ensure you have a Witness model defined
        fields = ['id', 'name', 'testimony', 'crime_record']
    
    def create(self, validated_data):
        # You can add any custom creation logic here if necessary
        witness = Witness.objects.create(**validated_data)
        return witness

