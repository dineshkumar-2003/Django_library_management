from django.contrib import admin
from Bookapp.models import Book,User,BookRequest

# Register your models here.
admin.site.register(Book)
admin.site.register(User)
admin.site.register(BookRequest)
