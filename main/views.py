from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import PesananEntryForm
from main.models import PesananEntry

def show_main(request):
    mood_entries = PesananEntry.objects.all()

    context = {
        'nama' : 'Daging Naga khas Sulawesi',
        'harga': 'Rp. 20.000',
        'description': 'Daging naga renyah dengan taburan darah kraken.',
        'rating' : '4.9/5.0',
        'quantity' : 'Maksimal 1 tiap transaksi.',
        'name' : 'Daniel Angger Dewandaru',
        'NPM' : '2306275973',
        'mood_entries': mood_entries
    }

    return render(request, "main.html", context)

def create_pesanan_entry(request):
    form = PesananEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_pesanan_entry.html", context)

def show_xml(request):
    data = PesananEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = PesananEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = PesananEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = PesananEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")