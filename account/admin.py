from django.contrib import admin
from account.models import Users,user_details

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
class UserAdmin(BaseUserAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('ID','email','is_admin','created_at','updated_at','is_deleted','password')
    list_filter = ('is_admin',)
    fieldsets = (
        ('User Credentials', {'fields': ('email','password')}),
        ('Permissions', {'fields': ('is_admin',)}),
        ('Details',{'fields': ('is_deleted',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','is_admin','is_deleted'),
        }),
    )
    search_fields = ('email',)
    ordering = ('created_at','ID')
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(Users, UserAdmin)

admin.site.register(user_details)