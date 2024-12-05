from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import CriminalRecord, Evidence, CrimeCategory, User
from django.contrib.auth.models import User as DjangoUser
from rest_framework.test import APIClient

class CriminalRecordTests(TestCase):

    def setUp(self):
        """
        Set up the test environment by creating test users and data.
        """
        self.client = APIClient()
        self.user = DjangoUser.objects.create_user(username="testuser", password="password")
        self.client.force_authenticate(user=self.user)

        # Create crime categories
        self.category1 = CrimeCategory.objects.create(name="Theft")
        self.category2 = CrimeCategory.objects.create(name="Assault")

        # Create a criminal record
        self.criminal_record = CriminalRecord.objects.create(
            first_name="John",
            last_name="Doe",
            gender="Male",
            date_of_birth="1990-01-01",
            crime_category=self.category1
        )

    def test_create_criminal_record(self):
        """
        Test if a criminal record can be created via API.
        """
        url = reverse('criminal-records-list')  # Assuming 'criminal-records-list' is your view name
        data = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'gender': 'Female',
            'date_of_birth': '1992-03-15',
            'crime_category': self.category2.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CriminalRecord.objects.count(), 2)

    def test_read_criminal_record(self):
        """
        Test if criminal record can be retrieved via API.
        """
        url = reverse('criminal-records-detail', kwargs={'pk': self.criminal_record.id})  # Assuming 'criminal-records-detail' is your view name
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], self.criminal_record.first_name)

    def test_update_criminal_record(self):
        """
        Test if a criminal record can be updated via API.
        """
        url = reverse('criminal-records-detail', kwargs={'pk': self.criminal_record.id})  # Assuming 'criminal-records-detail' is your view name
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'gender': 'Male',
            'date_of_birth': '1990-01-01',
            'crime_category': self.category2.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.criminal_record.refresh_from_db()
        self.assertEqual(self.criminal_record.crime_category, self.category2)

    def test_delete_criminal_record(self):
        """
        Test if a criminal record can be deleted via API.
        """
        url = reverse('criminal-records-detail', kwargs={'pk': self.criminal_record.id})  # Assuming 'criminal-records-detail' is your view name
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CriminalRecord.objects.count(), 0)

class EvidenceTests(TestCase):

    def setUp(self):
        """
        Set up test environment for Evidence.
        """
        self.client = APIClient()
        self.user = DjangoUser.objects.create_user(username="testuser", password="password")
        self.client.force_authenticate(user=self.user)

        # Create a criminal record and evidence
        self.criminal_record = CriminalRecord.objects.create(
            first_name="John",
            last_name="Doe",
            gender="Male",
            date_of_birth="1990-01-01",
            crime_category=CrimeCategory.objects.create(name="Theft")
        )
        self.evidence = Evidence.objects.create(
            evidence_type="Image",
            file="evidence1.jpg",
            criminal_record=self.criminal_record
        )

    def test_create_evidence(self):
        """
        Test if evidence can be uploaded via API.
        """
        url = reverse('evidence-list')  # Assuming 'evidence-list' is your view name
        data = {
            'evidence_type': 'Video',
            'file': 'evidence2.mp4',
            'criminal_record': self.criminal_record.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Evidence.objects.count(), 2)

    def test_read_evidence(self):
        """
        Test if evidence can be retrieved via API.
        """
        url = reverse('evidence-detail', kwargs={'pk': self.evidence.id})  # Assuming 'evidence-detail' is your view name
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['evidence_type'], self.evidence.evidence_type)

    def test_update_evidence(self):
        """
        Test if evidence can be updated via API.
        """
        url = reverse('evidence-detail', kwargs={'pk': self.evidence.id})  # Assuming 'evidence-detail' is your view name
        data = {
            'evidence_type': 'Document',
            'file': 'updated_evidence.pdf',
            'criminal_record': self.criminal_record.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.evidence.refresh_from_db()
        self.assertEqual(self.evidence.evidence_type, 'Document')

    def test_delete_evidence(self):
        """
        Test if evidence can be deleted via API.
        """
        url = reverse('evidence-detail', kwargs={'pk': self.evidence.id})  # Assuming 'evidence-detail' is your view name
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Evidence.objects.count(), 0)

class CrimeCategoryTests(TestCase):

    def setUp(self):
        """
        Set up the test environment for Crime Categories.
        """
        self.client = APIClient()
        self.user = DjangoUser.objects.create_user(username="testuser", password="password")
        self.client.force_authenticate(user=self.user)

        self.category = CrimeCategory.objects.create(name="Theft")

    def test_create_crime_category(self):
        """
        Test if crime category can be created via API.
        """
        url = reverse('crimecategory-list')  # Assuming 'crimecategory-list' is your view name
        data = {
            'name': 'Assault'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CrimeCategory.objects.count(), 2)

    def test_read_crime_category(self):
        """
        Test if crime category can be retrieved via API.
        """
        url = reverse('crimecategory-detail', kwargs={'pk': self.category.id})  # Assuming 'crimecategory-detail' is your view name
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.category.name)

    def test_update_crime_category(self):
        """
        Test if crime category can be updated via API.
        """
        url = reverse('crimecategory-detail', kwargs={'pk': self.category.id})  # Assuming 'crimecategory-detail' is your view name
        data = {
            'name': 'Fraud'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.category.refresh_from_db()
        self.assertEqual(self.category.name, 'Fraud')

    def test_delete_crime_category(self):
        """
        Test if crime category can be deleted via API.
        """
        url = reverse('crimecategory-detail', kwargs={'pk': self.category.id})  # Assuming 'crimecategory-detail' is your view name
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CrimeCategory.objects.count(), 0)

