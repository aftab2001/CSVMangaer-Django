from django.shortcuts import render
from .models import Item
from .resources import ItemResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
import csv,io
from django.core.paginator import Paginator
import csv
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
def upload(request):
    if request.method == 'POST':
        new_item = request.FILES.get('myfile')

        if not new_item or not new_item.name.endswith('.csv'):
            messages.error(request, 'Please upload a CSV file only.')
            return render(request, 'home.html')

        data_set = new_item.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)  # Skipping the header

        success_count = 0
        failure_count = 0

        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            try:
                # Basic validation (you can add more as needed)
                if not all(column):
                    raise ValueError("Missing data in one of the columns.")

                created, _ = Item.objects.update_or_create(
                    name=column[0],
                    description=column[1],
                    code=column[2],
                    quantity=column[3],
                    price=column[4],
                    vendor=column[5]
                )
                success_count += 1
            except Exception as e:
                # You can log the error if needed: print(str(e))
                failure_count += 1
                continue

        messages.success(request, f'File successfully uploaded. {success_count} rows were added/updated.')
        if failure_count > 0:
            messages.warning(request, f'{failure_count} rows failed to upload due to validation errors.')

        return render(request, 'home.html')

    return render(request, 'home.html')

def item_list_view(request):
    query_name = request.GET.get('name', '')
    query_code = request.GET.get('code', '')
    query_vendor = request.GET.get('vendor', '')
    export_format = request.GET.get('format','')

    items = Item.objects.all()

    if query_name:
        items = items.filter(name__icontains=query_name)
    if query_code:
        items = items.filter(code__icontains=query_code)
    if query_vendor:
        items = items.filter(vendor__icontains=query_vendor)
        
    if export_format == 'csv':
        return export_items_as_csv(items)
    elif export_format == 'pdf':
        return export_items_as_pdf(items)

    paginator = Paginator(items, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'items': page_obj,
        'query_name': query_name,
        'query_code': query_code,
        'query_vendor': query_vendor,
    }

    return render(request, 'items_list.html', context)
def export_items_as_csv(items):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="items.csv"'

    writer = csv.writer(response)
    writer.writerow(['Item Name', 'Item Code', 'Vendor Name'])

    for item in items:
        writer.writerow([item.name, item.code, item.vendor])

    return response

def export_items_as_pdf(items):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="items.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    p.drawString(100, 750, "Items List")

    y = 700
    for item in items:
        p.drawString(100, y, f"Name: {item.name}, Code: {item.code}, Vendor: {item.vendor}")
        y -= 20

    p.showPage()
    p.save()

    return response