from django.contrib import admin
from .models import  Controller
from .models import  EmbeddedLinux
from .models import  PcbDesigning
from .models import  WebApp


admin.site.register(Controller)
admin.site.register(EmbeddedLinux)
admin.site.register(PcbDesigning)
admin.site.register(WebApp)
