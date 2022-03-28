from logging.config import valid_ident
from multiprocessing.sharedctypes import Value
from turtle import penup
from urllib import request, response
from django.shortcuts import redirect, render, HttpResponse
from django.urls import is_valid_path
from perpustakaan.models import *
from perpustakaan.forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from perpustakaan.resource import BukuResource, KelompokResource
from django.contrib.auth.models import User
from tablib import Dataset





@login_required(login_url=settings.LOGIN_URL)
def home(request):
    template = 'home.html'
    return render(request, template)


@login_required(login_url=settings.LOGIN_URL)
def users(request):
    users = User.objects.all()
    template = 'users.html'
    context = {
        'users':users,
    }
    return render(request, template, context)



@login_required(login_url=settings.LOGIN_URL)
def hapus_users(request, id_user):
    users= User.objects.filter (id=id_user)
    users.delete()
    
    messages.success(request, "Data Berhasil dihapus!")
    return redirect ('users')



@login_required(login_url=settings.LOGIN_URL)
def export_xls(request):
    buku = BukuResource()
    dataset = buku.export()
    response = HttpResponse(dataset.xls, content_type = 'application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=laporan buku.xls'
    return response



@login_required(login_url=settings.LOGIN_URL)
def signup(request):
    if request.POST:
      form = UserCreationForm(request.POST)
      if form.is_valid():
          form.save()
          messages.success(request, "User berhasil dibuat!")
          return redirect('signup')
      else:
          messages.error(request, "Terjadi kesalahan!")
          return redirect('signup')
    else:
        form = UserCreationForm()
        konteks = {
            'form' : form,
        }
    return render(request, 'signup.html', konteks)




@login_required(login_url=settings.LOGIN_URL)
def buku(request):
    books = Buku.objects.all()
    

    konteks= {
        'books' : books,
    }
    return render(request, 'buku.html', konteks)
    

@login_required(login_url=settings.LOGIN_URL)
def ubah_buku(request, id_buku):
    buku = Buku.objects.get(id=id_buku)
    template = 'ubah-buku.html'
    if request.POST:
        form = FormBuku(request.POST, request.FILES, instance=buku)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Diperbaharui!")
            return redirect('ubah_buku', id_buku=id_buku)
    else:
        form = FormBuku(instance=buku)
        konteks = {
            'form' : form,
            'buku' : buku,   
        }
    return render(request, template, konteks)



@login_required(login_url=settings.LOGIN_URL)
def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormBuku()
            pesan = 'Data Berhasil Disimpan'

            konteks ={
                'form' : form,
                'pesan' : pesan,
            }
            return render(request, 'tambah-buku.html', konteks)
    

    else:
       form = FormBuku()

       konteks = {
           'form' : form,
       }
    return render(request, 'tambah-buku.html', konteks)   



@login_required(login_url=settings.LOGIN_URL)
def hapus_buku(request, id_buku):
    buku= Buku.objects.filter (id=id_buku)
    buku.delete()
    
    messages.success(request, "Data Berhasil dihapus!")
    return redirect ('buku')



@login_required(login_url=settings.LOGIN_URL)
def kelompok(request):
    group = Kelompok.objects.all()

    konteks = {
        'group' : group,
    }
    return render(request, 'kelompok.html', konteks)



@login_required(login_url=settings.LOGIN_URL)
def ubah_kelompok(request, id_kelompok):
    kelompok = Kelompok.objects.get(id=id_kelompok)
    template = 'ubah-kelompok.html'
    if request.POST:
        form = FormKelompok(request.POST, request.FILES, instance=kelompok)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Diperbaharui!")
            return redirect('ubah_kelompok', id_kelompok=id_kelompok)
    else:
        form = FormKelompok(instance=kelompok)
        konteks = {
            'form' : form,
            'kelompok' : kelompok,
        }
    return render(request, template, konteks)



@login_required(login_url=settings.LOGIN_URL)
def tambah_kelompok(request):
    if request.POST:
        form = FormKelompok(request.POST)
        if form.is_valid():
            form.save()
            form = FormKelompok()
            pesan = 'Data Berhasil Disimpan'

            konteks ={
                'form' : form,
                'pesan' : pesan,
            }
            return render(request, 'tambah-kelompok.html', konteks)
    

    else:
       form = FormKelompok()

       konteks = {
           'form' : form,
       }
    return render(request, 'tambah-kelompok.html', konteks) 


@login_required(login_url=settings.LOGIN_URL)
def hapus_kelompok(request, id_kelompok):
     kelompok= Kelompok.objects.filter (id=id_kelompok)
     kelompok.delete()
     return redirect ('kelompok')





@login_required(login_url=settings.LOGIN_URL)
def export_xlsx(request):
    kelompok = KelompokResource()
    dataset = kelompok.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Dsiposition'] = 'attachment; filename=kelompok.xls'
    return response