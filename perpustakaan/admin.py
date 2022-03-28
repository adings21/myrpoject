from django.contrib import admin
from perpustakaan.models import Buku, Kelompok
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class BukuAdmin(admin.ModelAdmin):
    list_display = ['judul', 'penulis', 'penerbit', 'jumlah']
    search_fields = ['judul', 'penulis', 'penerbit', 'jumlah']
    list_filter = ('kelompok_id',)
    list_per_page = 4



class KelompokAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Buku,BukuAdmin)
admin.site.register(Kelompok,KelompokAdmin)