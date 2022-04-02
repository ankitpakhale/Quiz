from django.contrib import admin
from .models import question,registerform,signupform
# Register your models here.
admin.site.register(question)
admin.site.register(registerform)

admin.site.register(signupform)