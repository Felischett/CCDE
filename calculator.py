def add(a, b):
    """
    Addiert zwei Zahlen und gibt das Ergebnis zurück.
    """
    return a + b

def subtract(a, b):
    """
    Subtrahiert b von a und gibt das Ergebnis zurück.
    """
    return a - b

def multiply(a, b):
    """
    Multipliziert zwei Zahlen und gibt das Ergebnis zurück.
    """
    return a * b
    
def divide(a, b):
    """
    Dividiert zwei Zahlen und gibt das Ergebnis zurück.
    """
    return a / b

if __name__ == "__main__":
    # Beispielausgaben
    print("5 + 3 =", add(5, 3))
    print("5 - 3 =", subtract(5, 3))
    print("5 * 3 =", multiply(5, 3))
    print("5 / 3 =", divide(5, 3))
    print("Hallo Felix")
