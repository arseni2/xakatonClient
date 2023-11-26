from django.urls import path
from .views import DocumentListCreateView, DocumentRetrieveUpdateDestroyView, process_data, add_additional_info, evaluate_loan_application, check_bki_status, calculate_pdn_view, calculate_pdn_view2

urlpatterns = [
    path('documents/', DocumentListCreateView.as_view(), name='document-list-create'),
    path('documents/process/', process_data, name='process-data'),
    path('documents/<int:pk>/', DocumentRetrieveUpdateDestroyView.as_view(), name='document-detail'),
    path('documents/<int:document_id>/add_additional_info/', add_additional_info, name='add_additional_info'),
    path('evaluate_loan_application/', evaluate_loan_application, name='evaluate_loan_application'),
    path('check_bki_status/', check_bki_status, name='check_bki_status'),
    path('calculate_pdn/', calculate_pdn_view, name='calculate_pdn'),
    path('calculate_pdn2/', calculate_pdn_view2, name='calculate_pdn2'),

    # Добавьте другие URL-маршруты при необходимости
]
