my_js = {
    "title": "title",
    "description": "Some description",
    "client": {
        "name": "Jon",
        "surname": "Karter",
        "phone": "+77777777777",
        "adress": "st. Mira, 287, Moscow"
    },
    "products": ["Candy", "Carrot", "Potato"],
    "delivery_adress": "st. Mira, 211, Ekaterinburg",
    "delivery_date": "2021-01-01:16:00",
    "delivery_code": "#232nkF3fAdn"
}

from bitrix24 import Bitrix24, BitrixError

bx24 = Bitrix24('https://b24-hzzdt4.bitrix24.kz/rest/1/23uqh8y0vqitp5pg/')

a = bx24.callMethod('crm.deal.list',
                order={'STAGE_ID': 'ASC'},
                filter={'>PROBABILITY': 50},
                select=['ID', 'TITLE', 'STAGE_ID', 'PROBABILITY'])

print(a)