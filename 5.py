# -*- coding: utf-8 -*-


# По адресу http://www.cbr.ru/scripts/XML_daily.asp находятся данные о курсе валют.
# Необходимо получить данные по соответствующему url и извлечь курс доллара и евро по отношению к рублю.

import requests
import xml.etree.ElementTree as et
from locale import setlocale, atof, LC_NUMERIC

CBR_URL = "http://www.cbr.ru/scripts/XML_daily.asp"
CURRENCY_LIST = ['EUR', 'USD']

# Чтобы корректно переводить курсы в float
setlocale(LC_NUMERIC, '')

xml_string = requests.get(CBR_URL).content

# Парсинг полученного XML
root = et.fromstring(xml_string)

currency = {valute.find('CharCode').text: atof(valute.find('Value').text)
            for valute in root
            if valute.find('CharCode').text in CURRENCY_LIST}
