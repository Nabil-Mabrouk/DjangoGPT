from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Learning, Config, Step, ModelConfig

admin.site.register(Learning)
admin.site.register(Config)
admin.site.register(Step)
admin.site.register(ModelConfig)