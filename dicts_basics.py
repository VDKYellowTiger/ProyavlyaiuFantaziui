# Словари.

character = {
    'hp': 100,
    'mana': 50,
    'ammo': {
        'left_hand': 'shield',
        'right_hand': 'sword',
    }
}

print(f'У персонажа {character["hp"]} здоровья и {character["mana"]} маны')

character['mana'] -= 20

print(f'У персонажа {character["hp"]} здоровья и {character["mana"]} маны')

print(f'Оружие. В правой руке {character["ammo"]["right_hand"]}')
print(f'Оружие. В левой руке {character["ammo"]["left_hand"]}')

print(f'Шлем {character.get("helm", "Отсутствует!")}')
print(f'Оружие {character.get("ammo", "Отсутствует!")}')

for key, value in character.items():
    print(key, value)

for key in character.keys():
    print(key)

for v in character.values():
    print(v)

print('helm' in character, 'hp' in character)