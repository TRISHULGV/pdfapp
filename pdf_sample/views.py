from django.shortcuts import render

from .models import Pdf
# Create your views here.

def index(request):
    pdf =  Pdf.objects.all()
    return render(request, 'pdf_sample/index.html',
    {
        'pdf_item' : pdf
    })
   