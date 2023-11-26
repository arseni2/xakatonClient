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


def risk_calc(age, family_status, having_children, credit_history, main_source, work_exp, pdn, revenue_client, savings):
    risk_points = 0
    if age is not None:
        age = int(age)
        if age < 25:
            risk_points += 5
        elif 26 <= age <= 55:
            risk_points += 1
        elif 56 <= age <= 74:
            risk_points += 3
        else:
            risk_points += 10

    if family_status.lower() == "холост":
        risk_points += 3
    elif family_status.lower() == "женат" or family_status.lower() == "замужем":
        risk_points += 2
    elif family_status.lower() == "в разводе":
        risk_points += 5

    if having_children.lower() == "да":
        risk_points += 3
    elif having_children.lower() == "нет":
        risk_points += 5

    if credit_history.lower() == "хорошая":
        risk_points += 1
    elif credit_history.lower() == "средняя":
        risk_points += 8
    elif credit_history.lower() == "плохая":
        risk_points += 15
    elif credit_history.lower() == "отсутствует":
        risk_points += 3

    if main_source.lower() == "заработная плата по основному месту работы":
        risk_points += 2
    elif main_source.lower() == "доходы от предпринимательства":
        risk_points += 7
    elif main_source.lower() == "пенсия":
        risk_points += 2
    elif main_source.lower() == "иное":
        risk_points += 15

    if work_exp is not None:
        work_exp = int(work_exp)
        if work_exp > 5:
            risk_points += 2
        elif 1 <= work_exp <= 5:
            risk_points += 3
        else:
            risk_points += 10

    if pdn is not None:
        pdn = int(pdn)
        if pdn > 95:
            risk_points += 20
        elif 70 <= pdn <= 95:
            risk_points += 10
        else:
            risk_points += 1

    if revenue_client is not None:
        revenue_client = int(revenue_client)
        if revenue_client > 250000:
            risk_points += 3
        elif 101000 <= revenue_client <= 250000:
            risk_points += 5
        elif 50000 <= revenue_client <= 100000:
            risk_points += 7
        else:
            risk_points += 15

    if savings.lower() == "да":
        risk_points += 1
    elif savings.lower() == "нет":
        risk_points += 5

    return risk_points

def calc_risk_level(risk_points):
    if risk_points <= 10:
        return "Низкий"
    elif 11 <= risk_points <= 20:
        return "Средний"
    elif 21 <= risk_points <= 30:
        return "Высокий"
    else:
        return "Очень высокий"



def make_credit_decision(age, family_status, having_children, credit_history, main_source, work_exp, pdn, revenue_client, savings):
    # Здесь ваша логика для принятия решения по выдаче кредита
    # Например:
    if risk_calc(age, family_status, having_children, credit_history, main_source, work_exp, pdn, revenue_client, savings) <= 15:
        return {'decision': 'Предоставить кредит', 'comment': 'Решение: Предоставить кредит. Клиент имеет низкий уровень риска.'}
    else:
        return {'decision': 'Отказать в предоставлении', 'comment': 'Решение: Отказать в предоставлении. Клиент имеет высокий уровень риска.'}