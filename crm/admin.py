from django.contrib import admin
from .models import User, Crime, CriminalRecord, Evidence, CrimeCategory, ReportingOfficer, CourtCase, Witness, PoliceStation, Complaint
from django.contrib.auth.models import Group

# Admin class for User model
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'role']
    search_fields = ['username', 'email']
    
    # Restrict users from seeing or modifying other users' data
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset  # Admins can see all users
        return queryset.filter(id=request.user.id)  # Regular users only see their own data
    
    def has_change_permission(self, request, obj=None):
        # Users can only edit their own profile
        if obj is None:
            return super().has_change_permission(request, obj)
        return obj.id == request.user.id or request.user.is_superuser
    
    def has_delete_permission(self, request, obj=None):
        # Users can only delete their own profile, or admins can delete anyone
        if obj is None:
            return super().has_delete_permission(request, obj)
        return obj.id == request.user.id or request.user.is_superuser

# Admin class for CriminalRecord model
class CriminalRecordAdmin(admin.ModelAdmin):
    list_display = ['case_number', 'suspect_name', 'crime_type', 'status', 'assigned_officer', 'date_reported']
    search_fields = ['case_number', 'suspect_name', 'crime_type__category_name']  # Search by crime category name
    list_filter = ['crime_type', 'status', 'assigned_officer']  # Correct the filter fields

    # Restrict permissions for non-admin users
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset  # Admins can see all criminal records
        return queryset.filter(reporting_officer=request.user.reportingofficer)  # Officers only see their own records

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return super().has_change_permission(request, obj)
        return obj.reporting_officer == request.user.reportingofficer or request.user.is_superuser
    
    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return super().has_delete_permission(request, obj)
        return obj.reporting_officer == request.user.reportingofficer or request.user.is_superuser

# Admin class for Evidence model
class EvidenceAdmin(admin.ModelAdmin):
    list_display = ['file', 'criminal_record', 'uploaded_by']
    search_fields = ['criminal_record__case_number', 'file']
    
    # Restrict permissions for non-admin users
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset  # Admins can see all evidence
        return queryset.filter(uploaded_by=request.user)  

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return super().has_change_permission(request, obj)
        return obj.uploaded_by == request.user or request.user.is_superuser
    
    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return super().has_delete_permission(request, obj)
        return obj.uploaded_by == request.user or request.user.is_superuser

# Admin class for CrimeCategory model
class CrimeCategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'description']  # Corrected the field name from 'name' to 'category_name'
    search_fields = ['category_name']  # Corrected search field name
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset  # All users can see crime categories, but not modify

    def has_add_permission(self, request):
        return request.user.is_superuser  # Only admins can add crime categories

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser  # Only admins can modify crime categories

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser  # Only admins can delete crime categories

# Admin class for ReportingOfficer model
class ReportingOfficerAdmin(admin.ModelAdmin):
    list_display = ['user', 'badge_number', 'department', 'date_of_hire']
    search_fields = ['user__username', 'badge_number']
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset  # Admins can see all reporting officers
        return queryset.filter(user=request.user)  # Officers only see their own data

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return super().has_change_permission(request, obj)
        return obj.user == request.user or request.user.is_superuser
    
    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return super().has_delete_permission(request, obj)
        return obj.user == request.user or request.user.is_superuser

# Admin class for CourtCase model
class CourtCaseAdmin(admin.ModelAdmin):
    list_display = ['case_number', 'court_name', 'hearing_date', 'judge', 'outcome', 'criminal_record']
    search_fields = ['case_number', 'court_name']
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset  # All users can see court cases

    def has_add_permission(self, request):
        return request.user.is_superuser  # Only admins can add court cases

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser  # Only admins can modify court cases

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser  # Only admins can delete court cases

# Admin class for Witness model
class WitnessAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_details', 'testimony', 'criminal_record']
    search_fields = ['name', 'criminal_record__case_number']
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset  # All users can see witnesses

    def has_add_permission(self, request):
        return request.user.is_superuser  # Only admins can add witnesses

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser  # Only admins can modify witnesses

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser  # Only admins can delete witnesses

# Admin class for PoliceStation model
class PoliceStationAdmin(admin.ModelAdmin):
    list_display = ['station_name', 'location']
    search_fields = ['station_name', 'location']
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset  # All users can see police stations

    def has_add_permission(self, request):
        return request.user.is_superuser  # Only admins can add police stations

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser  # Only admins can modify police stations

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser  # Only admins can delete police stations

# Admin class for Complaint model
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['complaint_type', 'complainant_name', 'status', 'submitted_at', 'criminal_record']
    search_fields = ['complaint_type', 'complainant_name']
    list_filter = ['status']
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset  # All users can see complaints

    def has_add_permission(self, request):
        return request.user.is_superuser  # Only admins can add complaints

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser  # Only admins can modify complaints

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser  # Only admins can delete complaints

# Registering the models with their custom admins
admin.site.register(User, UserAdmin)
admin.site.register(Crime)
admin.site.register(CriminalRecord, CriminalRecordAdmin)
admin.site.register(Evidence, EvidenceAdmin)
admin.site.register(CrimeCategory, CrimeCategoryAdmin)
admin.site.register(ReportingOfficer, ReportingOfficerAdmin)
admin.site.register(CourtCase, CourtCaseAdmin)
admin.site.register(Witness, WitnessAdmin)
admin.site.register(PoliceStation, PoliceStationAdmin)
admin.site.register(Complaint, ComplaintAdmin)

def has_module_permission(self, request, module):
    if module == 'criminal_records' and not request.user.is_superuser:
        return False
    return super().has_module_permission(request, module)
