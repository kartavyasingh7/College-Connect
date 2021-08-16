from django.contrib import admin
from .models import Student, buySell, FilesAdmin
# Register your models here.

admin.site.register(Student)
admin.site.register(buySell)
admin.site.register(FilesAdmin)