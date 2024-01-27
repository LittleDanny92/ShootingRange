from django.db import models

class Contact(models.Model):
    company_name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.company_name} | {self.phone_number}"
