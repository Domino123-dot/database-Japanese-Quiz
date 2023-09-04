from django.contrib import admin
from .models import *


admin.site.register(questions)
admin.site.register(changelog)
admin.site.register(DiscordBotRequests)