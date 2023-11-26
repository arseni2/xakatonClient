from datetime import datetime, timedelta



from datetime import datetime, timedelta

# Заглушка для получения отчета БКИ
def get_bki_report(applicant_id):
    # В реальном приложении здесь должен быть вызов API БКИ
    # Например, с использованием библиотеки requests
    # response = requests.get(f'https://bki-okb.ru/api/report?applicant_id={applicant_id}')
    # return response.json()

    # Заглушка: возвращаем статические данные для тестирования
    return {
        'score': 750,
        'obligations': [
            {
                'type': 'Кредит',
                'dates': {
                    'open': '2022-01-01',
                    'planned_close': '2023-01-01',
                    'actual_close': '2022-12-01'
                },
                'role': 'Заемщик',
                'status': 'Текущий',
                'amount': 10000,
                'interest_rate': 10,
                'remaining_balance': 5000,
                'overdue': {
                    '1_30_days': 0,
                    '31_60_days': 0,
                    '61_90_days': 0,
                    '91_150_days': 0,
                    '151_180_days': 0,
                    'over_180_days': 0
                }
            },
            # Дополнительные обязательства могут быть добавлены
        ],
        'timestamp': int(datetime.timestamp(datetime.now()))
    }

# Заглушка для проверки срока актуальности отчета
def is_report_valid(report_data, validity_period=14):
    report_timestamp = report_data.get('timestamp')

    if report_timestamp:
        report_datetime = datetime.fromtimestamp(report_timestamp)
        expiration_datetime = datetime.now() - timedelta(days=validity_period)
        return report_datetime >= expiration_datetime

    return False

# Ваш код, который будет использовать отчет БКИ
applicant_id = '12345'  # Пример идентификатора заявителя
current_report = get_bki_report(applicant_id)

# Проверяем срок актуальности отчета
if is_report_valid(current_report):
    print("Используем текущий отчет:")
    print(f"Скорбалл: {current_report['score']}")
    print("Информация об обязательствах:")
    for obligation in current_report['obligations']:
        print(f"Тип: {obligation['type']}, Статус: {obligation['status']}, Сумма: {obligation['amount']}")
else:
    print("Текущий отчет устарел. Получаем свежий отчет.")
    new_report = get_bki_report(applicant_id)
    # Ваш код для обработки свежего отчета

def check_bki(applicant_id):
    # В реальном приложении здесь должен быть вызов API БКИ
    # Например, с использованием библиотеки requests
    # response = requests.get(f'https://bki-okb.ru/api/check?applicant_id={applicant_id}')
    # return response.json()

    # Заглушка: возвращаем статический результат для тестирования
    return {
        'status': 'approved',
        'message': 'No negative information found in the credit bureau.'
    }


def is_pdn_valid(last_calculation_timestamp, validity_period=5):
    """
    Проверяет актуальность расчета ПДН.
    :param last_calculation_timestamp: Временная метка последнего расчета ПДН.
    :param validity_period: Период актуальности расчета в рабочих днях.
    :return: True, если расчет актуален, False в противном случае.
    """
    if last_calculation_timestamp:
        last_calculation_datetime = datetime.fromtimestamp(last_calculation_timestamp)
        expiration_datetime = datetime.now() - timedelta(days=validity_period)
        return last_calculation_datetime >= expiration_datetime

    return False

def calculate_pdn(income, current_obligations):
    """
    Рассчитывает ПДН (предельную долговую нагрузку).
    :param income: Доход заявителя.
    :param current_obligations: Текущие обязательства заявителя.
    :return: Значение ПДН.
    """
    # Ваш код расчета ПДН
    # ...

    # Возвращаем статическое значение для тестирования
    return 0.3  # Пример значения ПДН