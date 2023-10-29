from django.contrib import admin

# Register your models here.
from .models import Kecamatan, Kelurahan, Peserta, Pelatihan, Jenis_pelatihan, Bank, Status_pendaftaran, Pendaftaran

class Pendaftaransetting(admin.ModelAdmin) : 
    list_display = ["peserta", "pelatihan", "status"]

admin.site.register(Kecamatan)
admin.site.register(Kelurahan)
admin.site.register(Peserta)
admin.site.register(Pelatihan)
admin.site.register(Jenis_pelatihan)
admin.site.register(Bank)
admin.site.register(Status_pendaftaran)
admin.site.register(Pendaftaran, Pendaftaransetting)
