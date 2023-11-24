print("(1) Umrechnung von Celsius nach Kelvin ")
print("(2) Umrechnung von Celsius nach Fahrenheit ")
print("(3) Umrechnung von Kelvin nach Celsius ")
print("(4) Umrechnung von Kelvin nach Fahrenheit ")
print("(5) Umrechnung von Fahrenheit nach Celsius ")
print("(6) Umrechnung von Fahrenheit nach Kelvin ")
selection = "bimbambum"
celsius = "bimbambam"
kelvin = "bambambim"
fahrenheit = "bambimbam"
while isinstance(selection, str):
    try:
        selection = int(input("Wähle deine gewünschte Umrechnung : "))
    except:
        print("Gebe nur die Zahlen 1-6 ein")
match selection:
    case 1:
        while isinstance(celsius, str):
            try:
                celsius = float(input("Gebe deinen Celsiuswert an : "))
                result = celsius + 273.15
                print("Dein Celsiuswert ist ", result ,"in Kelvin.")    
            except:
                print("Gebe nur Zahlen an!")
    case 2:
        while isinstance(celsius, str):
            try:
                celsius = float(input("Gebe deinen Celsiuswert an : "))
                result = (celsius * 9/5) + 32
                print("Dein Celsiuswert ist ", result ,"in Fahrenheit.")   
            except:
                print("Gebe nur Zahlen an!")
    case 3:
        while isinstance(kelvin, str):
            try:
                kelvin = float(input("Gebe deinen Kelvinwert an : "))
                result = kelvin - 273.15
                print("Dein Kelvinwert ist ", result ,"in Celsius.")
            except:
                print("Gebe nur Zahlen von 0 aufwärts an!")
    case 4:
        while isinstance(kelvin, str):
            try:
                kelvin = float(input("Gebe deinen Kelvinwert an : "))
                result = (kelvin - 273.15) * 9/5 + 32
                print("Dein Kelvinwert ist ", result , "in Fahrenheit.")
            except:
                print("Gebe nur Zahlen von 0 aufwärts an!")
    case 5:
        while isinstance(fahrenheit, str):
            try:
                fahrenheit = float(input("Gebe deinen Fahrenheitwert an: "))
                result = (fahrenheit - 32) * 5/9
                print("Dein Fahrenheitwert ist ", result ,"in Celsius.")
            except:
                print("Gebe nur Zahlen an!")
    case 6:
        while isinstance(fahrenheit, str):
            try:
                fahrenheit = float(input("Gebe deinen Fahrenheitwert an: "))
                result = (fahrenheit - 32) * 5/9 + 273.15
                print("Dein Fahrenheitwert ist ", result , "in Kelvin.")
            except:
                print("Gebe nur Zahlen an!")
