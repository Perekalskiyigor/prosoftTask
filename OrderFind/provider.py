import requests
import json

# код

def OrderJsonData(order_number):
    """Получение всех данных по одному заказу и HTTP статус кода"""
    url = f"https://c.prosyst.ru/erp_game_razin/hs/rtk/order/{order_number}"
    auth = ('rtk', '387Keze')
    params = {'order': 'R878.2.1'}
    
    try:
        response = requests.get(url, auth=auth, params=params)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        
        data = json.loads(response.text)
        
        dict_ = {}
        
        # Номер заказа
        order = data['order']
        dict_['order'] = order
        
        # Имя заказа
        nameOrder = data['products']
        dict_['nameOrder'] = nameOrder['product']
        
        # Кол-во
        value = data['products']
        dict_['value'] = value['count']
        
        # Состав изделия
        components = data['components']
        dict_['components'] = components
        
        # Серийные номера
        serialNumbers = data['products']
        dict_['serialNumbers'] = serialNumbers['batch']
        
        return dict_, "200"
    
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return None, "500"
    
    except json.JSONDecodeError as e:
        print(f"Ошибка при декодировании JSON: {e}")
        return None, "500"
    
    except KeyError as e:
        print(f"Отсутствует ожидаемый ключ в JSON: {e}")
        return None, "400"
    
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
        return None, "500"


    """
    order_number = '22'
result_dict, status_code = OrderJsonData(order_number)

if result_dict is not None:
    print(f"Данные заказа: {result_dict}")
    print(f"HTTP статус код: {status_code}")
else:
    print("Не удалось получить данные или произошла ошибка.")
    """
