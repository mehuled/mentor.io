from django.contrib import admin
from mentorapp.models import TestModel, Student, Mentor

admin.site.register(Student)
admin.site.register(Mentor)
admin.site.register(TestModel)
