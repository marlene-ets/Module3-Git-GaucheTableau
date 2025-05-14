"""Ce programme va nous servir à saluer une personne"""


print('Bonjour à toi !')

ville = input('ou habitez vous?')


print("Vous habitez dans cette ville: ", ville)
#Demande si l'utilisateur préfère être tutoyé ou vouvoyé
preference = input('Entrez oui si vous préférez être vouvoyez : ')
if preference == 'oui':
    print('Bonjour à vous')
elif preference == 'non' :
    print('Bonjour à toi')
nom = input("Quel est votre nom? ")

print(nom)