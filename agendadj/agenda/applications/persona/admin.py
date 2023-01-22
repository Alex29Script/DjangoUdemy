from django.contrib import admin

from .models import Person,Hobby,Reunion

admin.site.register([Person,Hobby,Reunion])
