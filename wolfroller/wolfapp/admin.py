from django.contrib import admin
from .models import Question, Player, WolfNumber

# Register your models here.
admin.site.register(Question)
admin.site.register(Player)
admin.site.register(WolfNumber)