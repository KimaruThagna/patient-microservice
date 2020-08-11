from django.contrib import admin
from .models import Patient


# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "county", "patient_number")

    class Meta:
        model = Patient


admin.site.register(Patient, PatientAdmin)

# Register your models here.
