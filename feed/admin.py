from django.contrib import admin

# Register your models here.
from feed.models import RegisteredUser, FeedItem

class RegisteredUserAdmin(admin.ModelAdmin):
    """RegisteredUser admin model."""
    model = RegisteredUser

class FeedItemAdmin(admin.ModelAdmin):
    """FeedItem admin model."""
    model = FeedItem

admin.site.register(RegisteredUser, RegisteredUserAdmin)
admin.site.register(FeedItem, FeedItemAdmin)
