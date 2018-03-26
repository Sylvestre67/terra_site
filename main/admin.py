from django.contrib import admin
from .models import Name, Gender, NameInState, State

# Register your models here.
admin.site.register(Name)
admin.site.register(Gender)
admin.site.register(State)
admin.site.register(NameInState)
