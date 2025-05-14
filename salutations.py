"""Ce programme va nous servir à saluer une personne"""


print('Bonjour à toi !')

nas = input('Quel est ton numéro d''assurance sociale?')

if len(nas) != 9:
    print('Le NAS fourni est invalide.')
else:
    print('Merci')
