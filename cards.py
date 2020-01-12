from constants import GUITARS


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
