def eldont():
    elsoSzo = input("\tKérek egy szót: ")
    masodikSzo = input("\tKérek egy másik szót: ")
    print("I/a.")
    
    if len(elsoSzo) > len(masodikSzo):
        print(f"\tA hosszabb szó:{elsoSzo}")
    elif len(elsoSzo) < len(masodikSzo):
        print(f"\tA hosszabb szó: {masodikSzo}")
    else:
        print("Egyforma hosszúak")
    
    print("I/d.")
    print(f"\tKülönbségük: {abs(len(elsoSzo)-len(masodikSzo))}")

def egy():
    eldont()
