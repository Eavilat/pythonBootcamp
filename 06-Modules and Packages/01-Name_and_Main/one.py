def funcion():
    print("func() corriendo en one.py")

print("top-level print dentro de one.py")

if __name__ == "__main__":
    print("one.py esta corriendo directamente")
else:
    print("one.py esta importada de otro modulo")
