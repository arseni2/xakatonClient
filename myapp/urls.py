from django.urls import path
from .views import DocumentListCreateView, downloadFile_view, DocumentRetrieveUpdateDestroyView, process_data, add_additional_info, evaluate_loan_application, check_bki_status, calculate_pdn_view

urlpatterns = [
    path('documents/', DocumentListCreateView.as_view(), name='document-list-create'),
    path('documents/process/', process_data, name='process-data'),
    path('documents/<int:pk>/', DocumentRetrieveUpdateDestroyView.as_view(), name='document-detail'),
    path('documents/<int:document_id>/add_additional_info/', add_additional_info, name='add_additional_info'),
    path('evaluate_loan_application/', evaluate_loan_application, name='evaluate_loan_application'),
    path('check_bki_status/', check_bki_status, name='check_bki_status'),
    path('calculate_pdn/', calculate_pdn_view, name='calculate_pdn'),
    path('downloadFile/', downloadFile_view, name="downloadFile_view"),

    # Добавьте другие URL-маршруты при необходимости
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
