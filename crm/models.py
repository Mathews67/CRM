from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from datetime import datetime
from django.utils import timezone
from datetime import date

# Custom User Model for RBAC
class User(AbstractUser):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Reporting Officer', 'Reporting Officer'),
        ('Investigating Officer', 'Investigating Officer'),
    ]
    
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='crm_user_set',  # Unique related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='crm_user_permissions_set',  # Unique related_name
        blank=True
    )

    def __str__(self):
        return f"{self.username} - {self.role}"

# CrimeCategory Model
class CrimeCategory(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    name = models.CharField(max_length=255, default='Unnamed Category')  # Default value for 'name'

    def __str__(self):
        return self.category_name

    @staticmethod
    def predefined_data():
        return [
            {'category_name': 'Violent Crimes', 'description': 'Crimes involving physical harm or threat of harm to a person.'},
            {'category_name': 'Property Crimes', 'description': 'Crimes involving theft or damage to property.'},
            {'category_name': 'Drug-Related Crimes', 'description': 'Crimes involving illegal drugs or substances.'},
            {'category_name': 'White Collar Crimes', 'description': 'Crimes involving fraud, embezzlement, or other financial schemes.'},
        ]

    @classmethod
    def initialize_categories(cls):
        """
        This method will populate the database with predefined categories
        if they do not already exist.
        """
        for data in cls.predefined_data():
            # Use get_or_create to ensure unique categories
            cls.objects.get_or_create(**data)

# Crime Model
class Crime(models.Model):
    crime_name = models.CharField(max_length=255)
    crime_category = models.ForeignKey(CrimeCategory, on_delete=models.CASCADE)  # Added field
    description = models.TextField(default="No description provided.")  # Default value for existing rows
    status = models.CharField(max_length=50, choices=[('Open', 'Open'), ('Closed', 'Closed')], default='Open')  # Default 'Open' status
    date_reported = models.DateField(default=date.today)  # Default date for existing rows
    officer_assigned = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Officer can be null or blank
    years_of_imprisonment = models.PositiveIntegerField(default=0)  # Default value of 0 for years of imprisonment
    imprisonment_type = models.CharField(
        max_length=50,
        choices=[('Simple Imprisonment', 'Simple Imprisonment'), ('Hard Labour', 'Hard Labour')],
        default='Simple Imprisonment'  # Default 'Simple Imprisonment' for existing rows
    )

    def __str__(self):
        return self.crime_name

    @staticmethod
    def predefined_data():
        return [
            {'crime_name': 'Murder', 'category': 'Violent Crimes', 'description': 'Intentional killing of another person.', 'years_of_imprisonment': 15, 'imprisonment_type': 'Hard Labour'},
            {'crime_name': 'Armed Robbery', 'category': 'Violent Crimes', 'description': 'Robbery involving weapons or violence.', 'years_of_imprisonment': 10, 'imprisonment_type': 'Hard Labour'},
            {'crime_name': 'Theft', 'category': 'Property Crimes', 'description': 'Unlawful taking of another’s property.', 'years_of_imprisonment': 5, 'imprisonment_type': 'Simple Imprisonment'},
            {'crime_name': 'Fraud', 'category': 'White Collar Crimes', 'description': 'Deception for financial gain.', 'years_of_imprisonment': 7, 'imprisonment_type': 'Simple Imprisonment'},
        ]

    @classmethod
    def initialize_crimes(cls):
        for data in cls.predefined_data():
            category = CrimeCategory.objects.get(category_name=data.pop('category'))
            cls.objects.get_or_create(category=category, **data)

class PoliceStation(models.Model):
    station_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    officers_in_charge = models.ManyToManyField('Officer')
    phone_number = models.CharField(max_length=15)  # Adjust the length as needed for phone numbers
    name = models.CharField(max_length=255)  # The 'name' field can store an additional name, such as a department or title.

    def __str__(self):
        return self.station_name

class Officer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="officer")
    badge_number = models.CharField(max_length=100, unique=True)
    department = models.CharField(max_length=255, blank=True)
    date_of_hire = models.DateField(default=timezone.now)  # Default to current date
    first_name = models.CharField(max_length=100, default='Unknown')  # Default value for first_name
    last_name = models.CharField(max_length=100, default='Unknown')   # Default value for last_name
    rank = models.CharField(max_length=50, default='Unranked')         # Default value for rank
    police_station = models.ForeignKey(PoliceStation, on_delete=models.SET_NULL, null=True, blank=True)  # ForeignKey field

    def __str__(self):
        return f"Officer: {self.user.username} - Badge: {self.badge_number}"
# Evidence Model
def validate_file_type(value):
    """Validate uploaded file types."""
    valid_mime_types = [
        'video/mp4', 'video/x-matroska', 'video/x-msvideo',
        'audio/mpeg', 'audio/wav', 'audio/ogg',
        'application/pdf', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 
        'text/plain',
        'image/jpeg', 'image/png',
    ]
    if value.file.content_type not in valid_mime_types:
        raise ValidationError('Unsupported file type.')

class Evidence(models.Model):
    criminal_record = models.ForeignKey(
        'CriminalRecord', 
        on_delete=models.CASCADE, 
        related_name='evidence'
    )
    uploaded_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        limit_choices_to={'role': 'Reporting Officer'}
    )
    file = models.FileField(upload_to='evidence/', validators=[validate_file_type])
    description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Evidence for Case {self.criminal_record.case_number}"

# CriminalRecord Model
class CriminalRecord(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Under Investigation', 'Under Investigation'),
        ('Case Closed', 'Case Closed'),
    ]
    
    case_number = models.CharField(max_length=100, unique=True)
    suspect_name = models.CharField(max_length=200)
    crime_type = models.ForeignKey(Crime, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    date_reported = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')  # Default status to 'Pending'
    assigned_officer = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        limit_choices_to={'role': 'Investigating Officer'},  
        related_name='assigned_cases'
    )

    def __str__(self):
        return f"Case {self.case_number} - {self.suspect_name}"

    def clean(self):
        if self.assigned_officer and self.assigned_officer.role != 'Investigating Officer':
            raise ValidationError({'assigned_officer': 'The officer must be an Investigating Officer.'})

    class Meta:
        verbose_name = "Criminal Record"
        verbose_name_plural = "Criminal Records"
        ordering = ['-date_reported']

    def save(self, *args, **kwargs):
        if not self.case_number:  # If case_number is not provided, generate it
            current_year = datetime.now().year
            count = CriminalRecord.objects.filter(date_reported__year=current_year).count() + 1
            self.case_number = f"CR-{current_year}-{count:04d}"  # Format: CR-YYYY-XXXX
        self.full_clean()
        super().save(*args, **kwargs)

# ReportingOfficer Model
class ReportingOfficer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="reporting_officer")
    badge_number = models.CharField(max_length=100, unique=True)
    department = models.CharField(max_length=255, blank=True)
    date_of_hire = models.DateField(default=timezone.now)  # Default to current date
    first_name = models.CharField(max_length=100, default='Unknown')  # Default value for first_name
    last_name = models.CharField(max_length=100, default='Unknown')   # Default value for last_name
    rank = models.CharField(max_length=50, default='Unranked')         # Default value for rank
    police_station = models.ForeignKey('PoliceStation', on_delete=models.SET_NULL, null=True, blank=True)  # ForeignKey field to a PoliceStation model
    email = models.EmailField(max_length=255, blank=True)

    def __str__(self):
        return f"Reporting Officer: {self.user.username} - Badge: {self.badge_number}"


class Court(models.Model):
    name = models.CharField(max_length=255)  # Name of the court
    location = models.CharField(max_length=255)  # Physical location of the court
    contact_number = models.CharField(max_length=15, blank=True, null=True)  # Optional contact number
    email = models.EmailField(blank=True, null=True)  # Optional email address
    court_type = models.CharField(
        max_length=100,
        choices=[
            ('Civil', 'Civil'),
            ('Criminal', 'Criminal'),
            ('Family', 'Family'),
            ('Traffic', 'Traffic'),
            ('Appeals', 'Appeals')
        ],
        default='Civil'
    )  # Type of court (e.g., Civil, Criminal)
    judge_count = models.PositiveIntegerField(default=1)  # Number of judges in the court
    established_date = models.DateField()  # Date the court was established
    is_active = models.BooleanField(default=True)  # Whether the court is currently active or not

    def __str__(self):
        return self.name

# CourtCase Model
class CourtCase(models.Model):
    case_number = models.CharField(max_length=100, unique=True)
    court_name = models.CharField(max_length=255)
    hearing_date = models.DateField()
    judge = models.CharField(max_length=255)
    outcome = models.CharField(
        max_length=255,
        choices=[
            ('Guilty', 'Guilty'),
            ('Not Guilty', 'Not Guilty'),
            ('Pending', 'Pending')
        ],
        default='Pending'
    )
    criminal_record = models.ForeignKey('CriminalRecord', on_delete=models.CASCADE)
    
    # Adding missing fields
    date_filed = models.DateField()  # Date when the case was filed
    status = models.CharField(
        max_length=50,
        choices=[
            ('Active', 'Active'),
            ('Closed', 'Closed'),
            ('Pending', 'Pending'),
        ],
        default='Active',
    )  # Status of the case
    crime = models.ForeignKey('Crime', on_delete=models.CASCADE)  
    court = models.ForeignKey('Court', on_delete=models.CASCADE)  
    def __str__(self):
        return f"Court Case {self.case_number} - {self.outcome}"

# Witness Model
class Witness(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    statement = models.TextField()  # The statement of the witness
    contact_info = models.CharField(max_length=255)  # For witness contact information
    
    # Adding missing fields
    name = models.CharField(max_length=255, blank=True, null=True)  # Full name field if needed
    contact_details = models.CharField(max_length=255, blank=True, null=True)  # For extended contact details
    testimony = models.TextField(blank=True, null=True)  # Witness testimony text
    criminal_record = models.TextField(blank=True, null=True)  # Criminal record details

    # Foreign Key to CourtCase
    court_case = models.ForeignKey('CourtCase', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"  # Optional: Full name method if needed

    def get_contact_details(self):
        return self.contact_info  # Return contact details method

    def get_testimony(self):
        return self.testimony  # Return testimony method

    def get_criminal_record(self):
        return self.criminal_record  # Return criminal record method

class Complainant(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)  # Optional: you can add other details for the complainant.
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Complaint(models.Model):
    complaint_type = models.CharField(max_length=255)
    complainant_name = models.CharField(max_length=255)
    complainant = models.ForeignKey(Complainant, on_delete=models.CASCADE)  # Now this works because Complainant is defined above
    description = models.TextField()
    status = models.CharField(
        max_length=255,
        choices=[
            ('Open', 'Open'),
            ('Resolved', 'Resolved'),
            ('In Progress', 'In Progress')
        ],
        default='Open'
    )
    submitted_at = models.DateTimeField(auto_now_add=True)
    criminal_record = models.ForeignKey('CriminalRecord', on_delete=models.CASCADE)

    def __str__(self):
        return self.complainant_name



