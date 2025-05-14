"""Ce programme va nous servir à saluer une personne"""


#Demande si l'utilisateur préfère être tutoyé ou vouvoyé
preference = input('Entrez oui si vous préférez être vouvoyez : ')
if preference == 'oui':
    print('Bonjour à vous')
elif preference == 'non' :
    print('Bonjour à toi')
nom = input("Quel est votre nom? ")

print(nom)

nas = input(f'Quel est ton numéro d''assurance sociale, {nom}?')

if len(nas) != 9:
    print('Le NAS fourni est invalide.')
else:
    print('Merci')
