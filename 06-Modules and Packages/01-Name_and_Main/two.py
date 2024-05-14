import one

print("top-level en two.py")

one.func()

if __name__ == "__main__":
    print("two.py esta siendo corrida directamente")
else:
    print("two.py esta siendo importada de otro modulo")
