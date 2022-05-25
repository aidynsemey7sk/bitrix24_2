from bitrix24 import Bitrix24, BitrixError


class Btx:
    def __init__(self, webhook, input_data):
        self.bx24 = Bitrix24(webhook)
        self.input_data = input_data
        self.products = input_data['products']
        self.client = input_data['client']
        self.phone_client = input_data['client']['phone']
        self.delivery_code = input_data['delivery_code']

        # print(self.client['name'])
        # print(self.input_data['title'])
        # print(self.input_data['description'])

    def get_deal_list(self):
        deal_list = self.bx24.callMethod(
            'crm.deal.list',
            order={'STAGE_ID': 'ASC'},
            filter={'ID': 1},
            # select=['ID', 'TITLE', 'STAGE_ID', 'CLIENT']
        )
        return deal_list

    def add_deal_custom_fields(self):
        try:
            client = self.bx24.callMethod(
                'crm.deal.userfield.add',
                fields={
                    "FIELD_NAME": "PRODUCTS",
                    'USER_TYPE_ID': 'enumeration',


                    "LIST": [{"VALUE": "Элемент #1"},
                             {"VALUE": "Элемент #2"},
                             {"VALUE": "Элемент #3"}]
                },
            )
            return True
        except BitrixError as error:
            print(error)
            return False

    def add_deal(self):
        try:
            client = self.bx24.callMethod(
                'crm.deal.add',
                fields={
                    "TITLE": self.input_data['title'],
                    "ADDITIONAL_INFO": self.input_data['description'],
                    # "PRODUCTS": self.input_data["products"],
                    # "DELIVERY_ADDRESS": self.input_data['delivery_address'],
                    # "DELIVERY_DATE": self.input_data['delivery_date'],
                    # "DELIVERY_CODE": self.input_data['delivery_code'],
                }
            )
            return True
        except BitrixError as error:
            print(error)
            return False

    def get_client(self):
        client = self.bx24.callMethod(
            'crm.contact.list',
            order={'STAGE_ID': 'ASC'},
            filter={'PHONE': '+77711523694'},
            select=['ID', 'NAME', 'LAST_NAME', 'PHONE']
        )
        return client

    def add_client(self):
        try:
            client = self.bx24.callMethod(
                'crm.contact.add',
                fields={
                    'NAME': self.client['name'],
                    'LAST_NAME': self.client['surname'],
                    'PHONE': [{"VALUE": self.client['phone']}],
                    'ADDRESS': self.client['address'],
                }
            )
            print('Success added client')
            return True
        except BitrixError as error:
            print(error)
            return False

    def add_deal_client(self, client_id, deal_id):
        query = self.bx24.callMethod(
            'crm.deal.contact.add',
            id=deal_id,
            fields=client_id
        )
        return 'Success'

    def check_contact_for_b24(self) -> bool:
        contact = self.bx24.callMethod(
            'crm.contact.list',
            order={'STAGE_ID': 'ASC'},
            filter={'PHONE': f'{self.phone_client}'},
            select=['ID', 'NAME', 'LAST_NAME', 'HAS_PHONE', 'PHONE']
        )
        if contact:
            print(f'Клиент с номером {self.phone_client} его id: {contact[0]["ID"]} имя: {contact[0]["NAME"]}')
            return True
        else:
            print(f'Клинета с номером {self.phone_client} не существует его необходимо добавить в базу')
            return False

    def get_client_id(self) -> str:
        contact = self.bx24.callMethod(
            'crm.contact.list',
            filter={'PHONE': f'{self.phone_client}'},
            select=['ID']
        )
        return contact[0]['ID']

    def get_deal_id(self):
        deal_id = self.bx24.callMethod(
            'crm.deal.list',
            # order={'STAGE_ID': 'ASC'},
            filter={'DELIVERY_CODE': self.delivery_code},
            select=['ID']
        )
        return deal_id[0]['ID']

    def get_delivery_code(self):
        try:
            code = self.delivery_code
            return code
        except BitrixError as error:
            print(error)
            print("Необходимо заполнить поле delivery_code")
            return error

    def is_duplicate_deal_item(self):
        deal_id = self.bx24.callMethod(
            'crm.deal.list',
            # order={'STAGE_ID': 'ASC'},
            filter={'DELIVERY_CODE': self.delivery_code},
            select=['DELIVERY_ADDRESS', 'DELIVERY_DATE', 'DELIVERY_CODE']
        )
        return deal_id[0]



