def find_thief(person_a, person_b, person_c, n):
    if person_a >= n:
        print("Person A")
    elif person_b >= n:
        print("Person B")
    elif person_c >= n:
        print("Person C")
    else:
        print("Not found")


n = int(input("Amount stolen: "))
person_a = int(input("A: "))
person_b = int(input("B: "))
person_c = int(input("C: "))

find_thief(person_a=person_a,person_b=person_b,person_c=person_c, n = n)
