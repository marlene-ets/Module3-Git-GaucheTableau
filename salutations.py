"""Ce programme va nous servir à saluer une personne"""


print('Bonjour à toi !')

nom = input("Quel est votre nom? ")

print(nom)

nas = input(f'Quel est ton numéro d''assurance sociale, {nom}?')

if len(nas) != 9:
    print('Le NAS fourni est invalide.')
else:
    print('Merci')
