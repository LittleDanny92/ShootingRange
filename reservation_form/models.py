from django.db import models

class BookedDate(models.Model):
    datetime_field = models.DateTimeField()
    instructor_field = models.BooleanField(default=False)
    selected_weapon = models.CharField(max_length=100)
    name_field = models.CharField(max_length=100)
    email_field = models.CharField(max_length=100)

    def __str__(self):
        return self.datetime_field.strftime("%d.%m.%Y %H:%M")
