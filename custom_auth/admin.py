from django.contrib import admin
from .models import User 
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField



class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email_or_phone', 'first_name')
    list_filter = ('first_name',)
    fieldsets = (
        (None, {'fields': ('email_or_phone', 'password')}),
        ('Personal info', {'fields': ('first_name','last_name')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email_or_phone', 'password'),
        }),
    )
    search_fields = ('email_or_phone',)
    ordering = ('email_or_phone',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
