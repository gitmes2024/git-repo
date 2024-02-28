from django.contrib import admin
from .models import vconferencia
from .models import sala
from .models import tipoconf
from .models import departamento



# Register your models here.
admin.site.register(vconferencia)
admin.site.register(sala)
admin.site.register(tipoconf)
admin.site.register(departamento)
