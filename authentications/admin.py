from django.contrib import admin
from .models import *
from rest_framework.authtoken.models import TokenProxy

admin.site.unregister(TokenProxy)

admin.site.register(User)
admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(Entry)
admin.site.register(Post)
admin.site.register(Person)
admin.site.register(Group)
admin.site.register(Membership)
admin.site.register(City)
admin.site.register(Book)
admin.site.register(Student)
admin.site.register(Course)


admin.site.register(Topping)
admin.site.register(Pizza)