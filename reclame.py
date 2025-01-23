from algemene_functies import mijn_functie_2

def mijn_functie_2_lokaal(argument):
    teruggeefwaarden = {
        12.3: [15, 9, 36, 4],
        12.2: [14, 10, 24, 6],
        10.5: [15, 5, 50, 2],
        100.20: [120, 80, 2000, 5]
    }
    
    return teruggeefwaarden.get(argument, "Waarde niet gevonden")

resultaat = mijn_functie_2_lokaal(12.3)
print(resultaat)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer  
    
from typing import List, Tuple

def aanbieding_1(smaak: str, prijs: float, korting: float) -> str:
    nieuwe_prijs = prijs * (1 - korting)
    resultaat = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs:.2f} euro voor {nieuwe_prijs:.2f} euro."
    return resultaat

print(aanbieding_1("aardbei", 4, 0.1))

def inkomsten_totaal(inkomsten: List[float]) -> float:
    """Bereken het totaal van de inkomsten."""
    return sum(inkomsten)

def inkomsten_totaal_met_btw(inkomsten: List[float], btw: float) -> str:
    """Bereken het totaal van de inkomsten inclusief btw."""
    totaal = sum(inkomsten)
    bedrag_btw = totaal * btw
    uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal:.2f} euro, waarover {bedrag_btw:.2f} euro btw betaald dient te worden."
    return uitvoer

def laag_en_hoog(inkomsten: List[float]) -> Tuple[float, float]:
    """Bepaal het minimum en maximum van de inkomsten."""
    minimum = min(inkomsten)
    maximum = max(inkomsten)
    return minimum, maximum    

def gemiddelde(mijn_lijst: List[float]) -> float:
    """Bereken het gemiddelde van een lijst met zeven elementen."""
    if len(mijn_lijst) != 7:
        raise ValueError("De lijst moet precies zeven waarden bevatten.")
    
    if not all(isinstance(x, (int, float)) for x in mijn_lijst):
        raise TypeError("Alle elementen in de lijst moeten numeriek zijn.")
    
    totaal = sum(mijn_lijst)
    gemiddelde_waarde = totaal / len(mijn_lijst)
    
    return gemiddelde_waarde

def gemiddelde_inkomsten(inkomsten: List[float]) -> str:
    """Bereken het gemiddelde van de inkomsten."""
    if len(inkomsten) == 0:
        return "Geen inkomsten om het gemiddelde van te berekenen."
    
    gemiddeld = sum(inkomsten) / len(inkomsten)
    return f"De gemiddelde inkomsten deze week zijn {gemiddeld:.2f} euro."

def meervoudig(invoer_lijst: List[int]) -> List[int]:
    """Filter de even getallen uit de lijst."""
    if len(invoer_lijst) < 5 or len(invoer_lijst) > 10:
        raise ValueError("De lijst moet tussen de 5 en 10 integers bevatten.")
    
    meervouden = [x for x in invoer_lijst if x % 2 == 0]
    
    return meervouden

if __name__ == "__main__":
    week_inkomsten = [220, 430, 125, 160, 205, 90, 345]
    totaal = inkomsten_totaal(week_inkomsten)
    print(f"Totaal van de inkomsten deze week: {totaal:.2f} euro")
    
    inkomsten = [100, 200, 150]  
    btw_percentage = 0.09  
    print(inkomsten_totaal_met_btw(inkomsten, btw_percentage))
    
    uitvoer = laag_en_hoog(week_inkomsten)  
    print("Min en Max inkomsten:", uitvoer)  
    
    print("Het gemiddelde van de inkomsten is:", gemiddelde(week_inkomsten))
    
    print(gemiddelde_inkomsten(week_inkomsten))
    
    voorbeeld_lijst = [10, 5, 3, 2, 1, 2, 9]
    try:
        resultaat = meervoudig(voorbeeld_lijst)
        print("Meervouden van 2 in de lijst:", resultaat)
    except ValueError as e:
        print(e)
    
    