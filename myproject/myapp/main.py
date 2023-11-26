import pandas as pd
import os
#from myproject.settings import BASE_DIR

#print("BASE_DIR:", BASE_DIR)

def load_data_from_excel(file_path):
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"Ошибка при загрузке данных из Excel: {e}")
        return None

def check_required_fields(data_frame):
    required_fields = ["Паспортные данные", "Документ, подтверждающий доход"]
    for field in required_fields:
        if field not in data_frame.columns or data_frame[field].isnull().all():
            print(f"Внимание: Поле '{field}' не заполнено в Excel-файле.")
        else:
            print(f"Поле '{field}' заполнено в Excel-файле.")

def main():
    # ... (остальной код)

    # Загрузка данных из Excel и проверка заполненности полей
    # excel_file_path = os.path.join(BASE_DIR, 'docs/document.xlsx')  # Укажите правильный путь к файлу Excel
    excel_file_path = 'C:/Users/User/Desktop/pythonProject13/docs/document.xlsx'  # Укажите правильный путь к файлу Excel
    loaded_data = load_data_from_excel(excel_file_path)

    if loaded_data is not None:
        check_required_fields(loaded_data)

if __name__ == '__main__':
    main()