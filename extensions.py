import requests
import json

from config import API_PAS, keys


class APIException(Exception):
    pass


class RequestToApi:
    @staticmethod
    def get_price(*args):
        try:
            if len(args) != 3:
                raise APIException("Вы ввели неверный формат")
            elif args[0] not in keys or args[1] not in keys:
                raise APIException("Выберите доступную валюту")
            elif not args[2].isnumeric():
                raise APIException("Количество должно быть в цифрах")
            else:
                first_val, second_val, amount = args
                amount = int(amount)

                r = requests.get(f'https://api.apilayer.com/exchangerates_data/convert?'
                                 f'to={keys[second_val]}&from={keys[first_val]}&amount={amount}', headers=API_PAS)
                res = json.loads(r.content)

                return str(res['result'])

        except APIException as text:
            return text
        except Exception:
            return "Произошла ошибка. Пожалуйста попробуйте еще раз, соблюдая формат ввода."



