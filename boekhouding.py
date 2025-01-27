import csv

# Voorbeeld van de gegevens
inkomsten = {
    "Aardbeien-ijs-totaal": 1000,
    "Vanille-ijs-totaal": 2000,
    "Chocolade-ijs-totaal": 1500,
    "Waterijsjes-totaal": 750,
    'Salaris': 3000,
    'Verhuur': 1200,
    'Bijverdiensten': 500
}

# Bereken het totaal van de inkomsten
totaal_inkomsten = sum(inkomsten.values())

def presenteer(inkomsten, totaal):
    # Print de inkomsten
    for item, bedrag in inkomsten.items():
        print(f'"{item}": {bedrag},')
    # Print het totaal
    print(f'Totaal : {totaal} euro')

def schrijf_naar_csv(inkomsten, bestandsnaam='inkomsten.csv'):
    with open(bestandsnaam, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        for key, value in inkomsten.items():
            writer.writerow([key, value])

if __name__ == "__main__":
    # Aanroepen van de functie om te presenteren
    presenteer(inkomsten, totaal_inkomsten)
    # Aanroepen van de functie om naar CSV te schrijven
    schrijf_naar_csv(inkomsten)

