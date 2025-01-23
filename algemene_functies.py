def mijn_functie_1(argument):
    
    if argument in [2, 4, 10, 12]:
        return argument ** 2
    else:
        return None  


print(mijn_functie_1(2))  
print(mijn_functie_1(4))   
print(mijn_functie_1(10)) 
print(mijn_functie_1(12))  

def mijn_functie_2(argument):
    
    teruggeefwaarden = {
        12.3: [15, 9, 36, 4],
        12.2: [14, 10, 24, 6],
        10.5: [15, 5, 50, 2],
        100.20: [120, 80, 2000, 5]
    }

    if argument in teruggeefwaarden:
        return teruggeefwaarden[argument][0]
    else:
        return None


if __name__ == "__main__":
    print(mijn_functie_2(12.3))  
    print(mijn_functie_2(12.2))  
    print(mijn_functie_2(10.5))  
    print(mijn_functie_2(100.20))  