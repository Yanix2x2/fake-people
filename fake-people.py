import os
from random import randint, sample

from faker import Faker

import file_operations


LETTER_MAPPING = {
    'а': 'а͠',
    'б': 'б̋',
    'в': 'в͒͠',
    'г': 'г͒͠',
    'д': 'д̋',
    'е': 'е͠',
    'ё': 'ё͒͠',
    'ж': 'ж͒',
    'з': 'з̋̋͠',
    'и': 'и',
    'й': 'й͒͠',
    'к': 'к̋̋',
    'л': 'л̋͠',
    'м': 'м͒͠',
    'н': 'н͒',
    'о': 'о̋',
    'п': 'п̋͠',
    'р': 'р̋͠',
    'с': 'с͒',
    'т': 'т͒',
    'у': 'у͒͠',
    'ф': 'ф̋̋͠',
    'х': 'х͒͠',
    'ц': 'ц̋',
    'ч': 'ч̋͠',
    'ш': 'ш͒͠',
    'щ': 'щ̋',
    'ъ': 'ъ̋͠',
    'ы': 'ы̋͠',
    'ь': 'ь̋',
    'э': 'э͒͠͠',
    'ю': 'ю̋͠',
    'я': 'я̋',
    'А': 'А͠',
    'Б': 'Б̋',
    'В': 'В͒͠',
    'Г': 'Г͒͠',
    'Д': 'Д̋',
    'Е': 'Е',
    'Ё': 'Ё͒͠',
    'Ж': 'Ж͒',
    'З': 'З̋̋͠',
    'И': 'И',
    'Й': 'Й͒͠',
    'К': 'К̋̋',
    'Л': 'Л̋͠',
    'М': 'М͒͠',
    'Н': 'Н͒',
    'О': 'О̋',
    'П': 'П̋͠',
    'Р': 'Р̋͠',
    'С': 'С͒',
    'Т': 'Т͒',
    'У': 'У͒͠',
    'Ф': 'Ф̋̋͠',
    'Х': 'Х͒͠',
    'Ц': 'Ц̋',
    'Ч': 'Ч̋͠',
    'Ш': 'Ш͒͠',
    'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠',
    'Ы': 'Ы̋͠',
    'Ь': 'Ь̋',
    'Э': 'Э͒͠͠',
    'Ю': 'Ю̋͠',
    'Я': 'Я̋',
    ' ': ' ',
}

SKILLS = [
    'Стремительный прыжок',
    'Электрический выстрел',
    'Ледяной удар',
    'Стремительный удар',
    'Кислотный взгляд',
    'Тайный побег',
    'Ледяной выстрел',
    'Огненный заряд',
]


def get_cards(fake):
    for i in range(10):
        sample_SKILLS = sample(SKILLS, 3)
        ruined_sample_SKILLS = []

        for skill in sample_SKILLS:
            changed_letters = []
            for letter in skill:
                letter = LETTER_MAPPING[letter]
                changed_letters.append(letter)
            changed_skill = ''.join(changed_letters)
            ruined_sample_SKILLS.append(changed_skill)

        context = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'job': fake.job(),
            'town': fake.city(),
            'strength': randint(3, 18),
            'agility': randint(3, 18),
            'endurance': randint(3, 18),
            'intelligence': randint(3, 18),
            'luck': randint(3, 18),
            'skill_1': ruined_sample_SKILLS[0],
            'skill_2': ruined_sample_SKILLS[1],
            'skill_3': ruined_sample_SKILLS[2],
        }

        file_operations.render_template(
            'charsheet.svg', f'cards/result-{i}.svg', context
        )


if __name__ == '__main__':
    fake = Faker('ru_RU')
    os.makedirs('cards', exist_ok=True)
    get_cards(fake)
