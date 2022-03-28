from dataclasses import fields
from django.forms import ModelForm
from perpustakaan.models import Buku, Kelompok
from django import forms




class FormBuku(ModelForm):
    class Meta:
        model = Buku
        fields = '__all__'

        widgets = {
            'judul' : forms.TextInput({'class':'form-control'}),
            'penerbit' : forms.TextInput({'class':'form-control'}),
            'penulis' : forms.TextInput({'class':'form-control'}),
            'jumlah' : forms.NumberInput({'class':'form-control'}),
            'kelompok_id' : forms.Select({'class':'form-control'}),
        }



class FormKelompok(ModelForm):
    class Meta:
        model = Kelompok
        fields = '__all__'

        widgets = {
           'nama' : forms.TextInput({'class':'form-control'}),
           'keterangan' : forms.TextInput({'class':'form-control'}),
        }

