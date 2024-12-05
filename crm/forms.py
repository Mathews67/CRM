from django import forms
from .models import CrimeCategory, Crime, Officer, ReportingOfficer, CourtCase, Witness, PoliceStation, Complaint

# Forms for Crime Categories
class CrimeCategoryForm(forms.ModelForm):
    class Meta:
        model = CrimeCategory
        fields = ['category_name', 'description', 'name']

    # Custom validation for 'category_name' to ensure it is not empty
    def clean_category_name(self):
        category_name = self.cleaned_data.get('category_name')
        if not category_name:
            raise forms.ValidationError("Category name is required.")
        return category_name

    # Custom validation for 'name' to ensure it is not empty
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError("Name is required.")
        return name



# Forms for Crimes
class CrimeForm(forms.ModelForm):
    class Meta:
        model = Crime
        fields = ['crime_category', 'description', 'status', 'officer_assigned']

    # Custom validation for 'crime_category'
    def clean_crime_category(self):
        crime_category = self.cleaned_data.get('crime_category')
        if not crime_category:
            raise forms.ValidationError("Crime category is required.")
        return crime_category

    # Custom validation for 'status' to ensure it's a valid status
    def clean_status(self):
        status = self.cleaned_data.get('status')
        if status not in dict(Crime.STATUS_CHOICES):
            raise forms.ValidationError("Invalid status selected.")
        return status


# Forms for Officers
class OfficerForm(forms.ModelForm):
    class Meta:
        model = Officer
        fields = ['first_name', 'last_name', 'rank', 'police_station']

    # Custom validation for 'rank' to ensure it is not empty
    def clean_rank(self):
        rank = self.cleaned_data.get('rank')
        if not rank:
            raise forms.ValidationError("Officer rank is required.")
        return rank


# Forms for Reporting Officers
class ReportingOfficerForm(forms.ModelForm):
    class Meta:
        model = ReportingOfficer
        fields = [
            'user', 
            'badge_number', 
            'department', 
            'date_of_hire', 
            'first_name', 
            'last_name', 
            'rank', 
            'police_station', 
            'email'
        ]
    # Custom validation for 'email'
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email is required.")
        return email


# Forms for Court Cases
class CourtCaseForm(forms.ModelForm):
    class Meta:
        model = CourtCase
        fields = ['case_number', 'date_filed', 'crime', 'court', 'status']

    # Custom validation for 'case_number'
    def clean_case_number(self):
        case_number = self.cleaned_data.get('case_number')
        if not case_number:
            raise forms.ValidationError("Case number is required.")
        return case_number

    # Custom validation for 'status'
    def clean_status(self):
        status = self.cleaned_data.get('status')
        if status not in dict(CourtCase.STATUS_CHOICES):
            raise forms.ValidationError("Invalid case status.")
        return status


# Forms for Witnesses
class WitnessForm(forms.ModelForm):
    class Meta:
        model = Witness
        fields = ['first_name', 'last_name', 'contact_info', 'statement']

    # Custom validation for 'statement'
    def clean_statement(self):
        statement = self.cleaned_data.get('statement')
        if not statement:
            raise forms.ValidationError("Witness statement is required.")
        return statement


# Forms for Police Stations
class PoliceStationForm(forms.ModelForm):
    class Meta:
        model = PoliceStation
        fields = ['name', 'location', 'phone_number']

    # Custom validation for 'phone_number'
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number:
            raise forms.ValidationError("Phone number is required.")
        return phone_number


# Forms for Complaints
class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['complainant', 'complaint_type', 'description', 'status']

    # Custom validation for 'complainant'
    def clean_complainant(self):
        complainant = self.cleaned_data.get('complainant')
        if not complainant:
            raise forms.ValidationError("Complainant information is required.")
        return complainant

    # Custom validation for 'status'
    def clean_status(self):
        status = self.cleaned_data.get('status')
        if status not in dict(Complaint.STATUS_CHOICES):
            raise forms.ValidationError("Invalid status for complaint.")
        return status
