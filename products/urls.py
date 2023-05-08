from django.urls import path
from products.views import ProductsView, ExportToPdf, ExportToCSV, ImportCSV, ProductDetail

urlpatterns = [
    path('', ProductsView.as_view(), name='products'),
    path('<uuid:pk>', ProductDetail.as_view(), name='product'),
    path('export-csv/', ExportToCSV.as_view(), name='products_to_csv'),
    path('export-pdf/', ExportToPdf.as_view(), name='products_to_pdf'),
    path('import-csv/', ImportCSV.as_view(), name='products_from_csv'),
]
