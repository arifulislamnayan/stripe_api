from django.contrib import admin
from profiles.models import profile


class ProfileAdmin(admin.ModelAdmin):
	class Meta:
		model = profile




admin.site.register(profile, ProfileAdmin)



# Register your models here.
