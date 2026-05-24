from django.shortcuts import render

def gst(request):

    price = ""
    gst_per = ""
    bill = ""

    if request.method == "POST":

        price = request.POST['price']
        gst_per = request.POST['gst']

        total = float(price) + (float(price) * float(gst_per) / 100)

        bill = total

    return render(request, 'math.html', {
        'price': price,
        'gst_per': gst_per,
        'bill': bill
    })