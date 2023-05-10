from django.contrib import admin
from stgcs_admin.models import student_registration,login_details,teachers_registration,non_teaching,school_management,approved_teachers,lower_primary,upper_primary,secodary,higher_secondary
admin.site.register(student_registration) # Employee is registered
admin.site.register(login_details)
admin.site.register(teachers_registration)
admin.site.register(non_teaching)
admin.site.register(school_management)
admin.site.register(approved_teachers)
admin.site.register(lower_primary)
admin.site.register(upper_primary)
admin.site.register(secodary)
admin.site.register(higher_secondary)
