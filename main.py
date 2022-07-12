import random

def randomizza(lst):
    while True:
        try:
            n = round(random.randint(0, len(lst)-1))
        except:
            lst = crealista("questions.txt")
            print("---------------Questions are over, press Enter to restart with a different order---------------")
            pause = input()
            
        elemento = lst[n]
        lst.remove(elemento)
        lenDom = len(lst)
        print("\n" + elemento)
        print("Questions left: {}".format(lenDom) )
        pause = input()
    return elemento


def crealista(ftesto):
    with open(ftesto, encoding="utf8") as f:
        f =f.read()
        lst = f.split("\n")
        lst = [i for i in lst if i != ""]
    return lst

lst = crealista("questions.txt")
randomizza(lst)


