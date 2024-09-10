from django.shortcuts import render

def show_main(request):
    context = {
        'nama' : 'Daging Naga khas Sulawesi',
        'harga': 'Rp. 20.000',
        'description': 'Daging naga renyah dengan taburan darah kraken.',
        'rating' : '4.9/5.0',
        'quantity' : 'Maksimal 1 tiap transaksi.'
    }

    return render(request, "main.html", context)
