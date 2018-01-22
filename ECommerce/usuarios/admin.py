from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
 
from .models import CustomUser, LinkedInUser
from .forms import CustomUserCreationForm, LinkedInUserCreationForm
 
class CustomUserAdmin(UserAdmin):
    form = CustomUserCreationForm
 
admin.site.register(CustomUser, CustomUserAdmin)

class LinkedInUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'linkedin_id',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'linkedin_id', 'password1', 'password2')}
        ),
    )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('linkedin_id', 'first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    form = LinkedInUserCreationForm
 
admin.site.register(LinkedInUser, LinkedInUserAdmin)
 
