from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Item)
admin.site.register(Movie)
admin.site.register(Resource)
