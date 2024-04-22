from html_templates import index_template
from api_requests import get_birds_data
from data_processing import generate_bird_cards

def main():
    url = 'https://aves.ninjas.cl/api/birds'
    birds_data = get_birds_data(url)
    if birds_data:
        bird_cards = generate_bird_cards(birds_data)
        html_content = index_template.substitute(bird_cards=bird_cards)
        with open('aves_de_chile.html', 'w') as f:
            f.write(html_content)
        print("Sitio web generado correctamente. Puede encontrarlo en el archivo 'aves_de_chile.html'.")

if __name__ == "__main__":
    main()
