from django.contrib import admin
from .models import Question, Player, WolfNumber, RoleAssignment

# Register your models here.
admin.site.register(Question)
admin.site.register(Player)
admin.site.register(WolfNumber)
admin.site.register(RoleAssignment)