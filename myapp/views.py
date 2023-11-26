from .models import Document, AdditionalInfo
from .serializers import DocumentSerializer, AdditionalInfoSerializer
from django.http import JsonResponse
import pandas as pd
import traceback
from django.shortcuts import render
from .utils import get_bki_report, is_report_valid, check_bki
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Document
from .serializers import DocumentSerializer
from datetime import datetime, timedelta
from .utils import is_pdn_valid, calculate_pdn
from rest_framework import generics
from rest_framework.response import Response
from .models import Document
from .serializers import DocumentSerializer

def calculate_pdn_view(request):
    try:
        # Здесь проведите расчет ПДН и подготовьте данные для вывода
        income = 50000  # Замените на фактические данные
        current_obligations = 20000  # Замените на фактические данные

        # Здесь нужно хранить временную метку последнего расчета
        last_calculation_timestamp = datetime.timestamp(datetime.now())

        if not is_pdn_valid(last_calculation_timestamp):
            # Проведите новый расчет ПДН
            pdn_value = calculate_pdn(income, current_obligations)

            # Сохраните результаты расчета, включая временную метку
            last_calculation_timestamp = datetime.timestamp(datetime.now())
            # Сохраните pdn_value и last_calculation_timestamp в базу данных или другое хранилище

        pdn_value = calculate_pdn(income, current_obligations)

        # Возвращаем результат в формате JSON
        response_data = {
            'income': income,
            'current_obligations': current_obligations,
            'pdn_value': pdn_value,
            'last_calculation_timestamp': last_calculation_timestamp
        }

        return JsonResponse(response_data)
    except Exception as e:
            # Вывести подробности об ошибке
            return JsonResponse({'error': str(e)}, status=500)
class DocumentListCreateView(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
class DocumentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
@api_view(['GET', 'POST'])
def check_bki_status(request):
    applicant_id = '12345'

    if request.method == 'GET':
        current_report = get_bki_report(applicant_id)

        if is_report_valid(current_report):
            response_data = {
                'applicant_id': applicant_id,
                'bki_status': True,
                'message': 'Using current report for evaluation.',
                'score': current_report['score'],
                'obligations': current_report['obligations']
            }
        else:
            response_data = {
                'applicant_id': applicant_id,
                'bki_status': False,
                'message': 'Current report is outdated. Obtaining a fresh report.'
            }

        return JsonResponse(response_data)

    elif request.method == 'POST':
        current_report = get_bki_report(applicant_id)

        if is_report_valid(current_report):
            context = {
                'applicant_id': applicant_id,
                'bki_status': True,
                'message': 'Using current report for evaluation.',
                'score': current_report['score'],
                'obligations': current_report['obligations']
            }
        else:
            context = {
                'applicant_id': applicant_id,
                'bki_status': False,
                'message': 'Current report is outdated. Obtaining a fresh report.'
            }

        return render(request, 'bki_status.html', context)





@api_view(['POST'])
def process_data(request):
    if request.method == 'POST' and request.FILES.get('excel_file'):
        excel_file = request.FILES['excel_file']
        
        # Проверяем, что загруженный файл - это Excel-файл
        if excel_file.name.endswith('.xlsx') or excel_file.name.endswith('.xls'):
            try:
                # Используем pandas для чтения содержимого Excel-файла
                df = pd.read_excel(excel_file)
                
                # Далее можно обработать содержимое файла (например, сохранить его в базу данных, выполнить вычисления и т.д.)
                
                # Возвращаем какой-то результат обработки (в данном случае отправляем количество строк и столбцов)
                return JsonResponse({'rows': len(df), 'columns': len(df.columns)})
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'Неверный формат файла. Пожалуйста, загрузите Excel-файл (.xlsx, .xls)'}, status=400)
    else:
        return JsonResponse({'error': 'Запрос должен быть типа POST и содержать файл Excel'}, status=400)

@api_view(['POST'])
def add_additional_info(request, document_id):
    try:
        document = Document.objects.get(pk=document_id)
    except Document.DoesNotExist:
        return Response({'message': 'Document not found'}, status=status.HTTP_404_NOT_FOUND)

    info_text = request.data.get('info_text', '')
    additional_info = AdditionalInfo.objects.create(document=document, info_text=info_text)

    serializer = AdditionalInfoSerializer(additional_info)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def evaluate_loan_application(request):
    applicant_id = request.data.get('applicant_id')

    if not applicant_id:
        return JsonResponse({'message': 'Missing applicant_id'}, status=400)

    current_report = get_bki_report(applicant_id)

    if is_report_valid(current_report):
        return JsonResponse({'message': 'Using current report for evaluation.'})
    else:
        new_report = get_bki_report(applicant_id)
        return JsonResponse({'message': 'Using a fresh report for evaluation.'})

def load_data_from_excel(file_path):
    try:
        df = pd.read_excel(file_path)
        print("Loaded data from Excel:")
        print(df.head())
        return df
    except ImportError:
        print("Ошибка: 'openpyxl' не установлен. Установите его с помощью 'pip install openpyxl'.")
        return None
    except Exception as e:
        print(f"Ошибка при загрузке данных из Excel: {e}")
        print(traceback.format_exc())
        return None

def check_required_fields(data_frame):
    required_fields = ["Паспортные данные", "Документ, подтверждающий доход"]
    result_data = {}

    for field in required_fields:
        if field not in data_frame.columns or data_frame[field].isnull().all():
            result_data[f"Внимание: Поле '{field}'"] = "не заполнено в Excel-файле."
        else:
            result_data[f"Поле '{field}'"] = "заполнено в Excel-файле."

    return result_data

@api_view(['GET'])
def downloadFile_view(request):
    # Ваш существующий код
    response_data = {
        'message': 'Success',
    }
    return JsonResponse(response_data, safe=False)