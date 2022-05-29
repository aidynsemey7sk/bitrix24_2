# Первая сделка без контакта
js_01 = {
    "title": "js_01",
    "description": "Первая сделка без контакта",
    "client": {
        "name": "Jon",
        "surname": "Karter",
        "phone": "+77777777777",
        "address": "st. Mira, 287, Moscow"
    },
    "products": ["Candy", "Carrot", "Potato"],
    "delivery_address": "st. Mira, 211, Ekaterinburg",
    "delivery_date": "2021-01-01:16:00",
    "delivery_code": "232nkF3fAdn"
}

# Вторая сделка с существующим контактом
js_02 = {
    "title": "js_02",
    "description": "Вторая  сделка с существующим контактом"
                   "delivery_code не совпадает ни с одной сделкой",
    "client": {
        "name": "Jon",
        "surname": "Karter",
        "phone": "+77777777777",
        "address": "st. Mira, 287, Moscow"
    },
    "products": ["Candy", "Carrot", "Potato"],
    "delivery_address": "st. Mira, 211, Ekaterinburg",
    "delivery_date": "2021-01-01:16:00",
    "delivery_code": "862Dw14vmFP"
}

# Пробуем создать дубликат
js_03 = {
    "title": "js_03",
    "description": "Пробуем создать дубликат",
    "client": {
        "name": "Jon",
        "surname": "Karter",
        "phone": "+77777777777",
        "address": "st. Mira, 287, Moscow"
    },
    "products": ["Candy", "Carrot", "Potato"],
    "delivery_address": "st. Mira, 211, Ekaterinburg",
    "delivery_date": "2021-01-01:16:00",
    "delivery_code": "862Dw14vmFP"
}

# Новая сделка с другими продуктами
js_04 = {
    "title": "js_04",
    "description": "Новая сделка с другими продуктами",
    "client": {
        "name": "Jon",
        "surname": "Karter",
        "phone": "+77777777777",
        "address": "st. Mira, 287, Moscow"
    },
    "products": ["Candy", "Tea", "Lemon"],
    "delivery_address": "st. Mira, 211, Ekaterinburg",
    "delivery_date": "2021-01-01:16:00",
    "delivery_code": "862Dw14vmFP"
}

# Новая сделка с другой датой
js_05 = {
    "title": "js_05",
    "description": "Новая сделка с другой датой",
    "client": {
        "name": "Jon",
        "surname": "Karter",
        "phone": "+77777777777",
        "address": "st. Mira, 287, Moscow"
    },
    "products": ["Candy", "Carrot", "Potato"],
    "delivery_address": "st. Mira, 211, Ekaterinburg",
    "delivery_date": "2022-10-08:16:00",
    "delivery_code": "862Dw14vmFP"
}

# Новая сделка с другим адресом
js_06 = {
    "title": "js_06",
    "description": "Новая сделка с другим адресом",
    "client": {
        "name": "Jon",
        "surname": "Karter",
        "phone": "+77777777777",
        "address": "st. Mira, 287, Moscow"
    },
    "products": ["Candy", "Carrot", "Potato"],
    "delivery_address": "st. Lenina, 211, Omsk",
    "delivery_date": "2021-01-01:16:00",
    "delivery_code": "862Dw14vmFP"
}

# Новая сделка и новый контакт
js_07 = {
    "title": "js_07",
    "description": "Новая сделка и новый контакт",
    "client": {
        "name": "Jim",
        "surname": "Carrey",
        "phone": "+70550130100",
        "address": "st. Mira, 287, Moscow"
    },
    "products": ["Candy", "Carrot", "Potato"],
    "delivery_address": "st. Mira, 211, Omsk",
    "delivery_date": "2021-12-04:16:00",
    "delivery_code": "sda7516gsabhd126"
}

# Обновление данных
js_08 = {
    "title": "js_07",
    "description": "Обновление данных",
    "client": {
        "name": "Jim",
        "surname": "Carrey",
        "phone": "+70550130100",
        "address": "st. Mira, 287, Moscow"
    },
    "products": ["Tea", "Milk", "Apple"],
    "delivery_address": "st. Pushkin, 211, Volgograd",
    "delivery_date": "2022-03-22:16:00",
    "delivery_code": "sda7516gsabhd126"
}


my_data_list = [js_01, js_02, js_03, js_04, js_05, js_06, js_07, js_08]