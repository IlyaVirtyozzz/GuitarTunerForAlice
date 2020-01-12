from states import *

GUITARS = [
    {
        'name': 'Акустическая',
        'icon': '213044/bea4dba88928102ebccb',
        'state': STATE_ACOUSTIC,
        'strings': {
            '1': 'sound1',
            '2': 'sound2',
            '3': 'sound3',
            '4': 'sound4',
            '5': 'sound5',
            '6': 'sound6',
        }
    },
    {
        'name': 'Классическая',
        'icon': '213044/bea4dba88928102ebccb',
        'state': STATE_CLASSIC,
        'strings': {
            '1': 'sound1',
            '2': 'sound2',
            '3': 'sound3',
            '4': 'sound4',
            '5': 'sound5',
            '6': 'sound6',
        }
    },
    {
        'name': 'Бас-гитара',
        'icon': '213044/bea4dba88928102ebccb',
        'state': STATE_BAS,
        'strings': {
            '1': 'sound1',
            '2': 'sound2',
            '3': 'sound3',
            '4': 'sound4'
        }
    },
    {
        'name': 'Электрогитара',
        'icon': '213044/bea4dba88928102ebccb',
        'state': STATE_ELECTRO,
        'strings': {
            '1': 'sound1',
            '2': 'sound2',
            '3': 'sound3',
            '4': 'sound4',
            '5': 'sound5',
            '6': 'sound6',
        }
    }
]


def get_menu_card(text):
    return {
        'type': 'ItemsList',
        'header': {
            'text': text
        },
        'items': [
            {
                'title': guitar['name'],
                'image_id': guitar['icon'],
                'button': {
                    'text': guitar['name'],
                    'payload': {
                        'text': guitar['name']
                    }
                }
            } for guitar in GUITARS]
    }, ', '.join([guitar['name'] for guitar in GUITARS])
