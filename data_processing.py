from html_templates import bird_card_template

def generate_bird_cards(birds_data):
    bird_cards = ''
    for bird in birds_data:
        bird_cards += bird_card_template.substitute(
            image=bird['images']['main'],
            nombre_espanol=bird['name']['spanish'],
            nombre_ingles=bird['name']['english']
        ) + '\n'
    return bird_cards
