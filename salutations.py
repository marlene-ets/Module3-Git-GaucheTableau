"""Ce programme va nous servir à saluer une personne"""

# Ligne d'etoiles
print('***')
print('Bonjour à toi !')



#Demande si l'utilisateur préfère être tutoyé ou vouvoyé
preference = input('Entrez oui si vous préférez être vouvoyez : ')
if preference == 'oui':
    print('Bonjour à vous')
elif preference == 'non' :
    print('Bonjour à toi')

# Demande nom
nom = input("Quel est votre nom? ")
print(nom)
