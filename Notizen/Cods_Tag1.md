## Code

    hoehe = 5

    for i in range(1, hoehe + 1):
        print("X" * i)

    X
    XX
    XXX
    XXXX
    XXXXX

    hoehe = 5

    for i in range(1, hoehe + 1):
        print(" " * (hoehe - i) + "X" * i)

        X
       XX
      XXX
     XXXX
    XXXXX


    hoehe = 5

    for i in range(hoehe):
        print(" " * (hoehe - i - 1) + "X" * (2 * i + 1))

        X
       XXX
      XXXXX
     XXXXXXX
    XXXXXXXXX

    import string

    for zeile in range(8, 0, -1):
        for spalte in string.ascii_lowercase[:8]:
            print(spalte + str(zeile), end=" ")
        print()

    a8 b8 c8 d8 e8 f8 g8 h8
    a7 b7 c7 d7 e7 f7 g7 h7
    a6 b6 c6 d6 e6 f6 g6 h6
    a5 b5 c5 d5 e5 f5 g5 h5
    a4 b4 c4 d4 e4 f4 g4 h4
    a3 b3 c3 d3 e3 f3 g3 h3
    a2 b2 c2 d2 e2 f2 g2 h2
    a1 b1 c1 d1 e1 f1 g1 h1


    zahlen = [1, 2, 3, 4, 5, 6]

    summe = 0

    for zahl in zahlen:
        summe += zahl
    print(summe)

    21

    for zahl in range(10):
    if zahl % 2 == 0:
        print(zahl, "ist gerade")
    else:
        print(zahl, "ist ungerade")
    
    0 ist gerade
    1 ist ungerade
    2 ist gerade
    3 ist ungerade
    4 ist gerade
    5 ist ungerade
    6 ist gerade
    7 ist ungerade
    8 ist gerade
    9 ist ungerade

    punkte = [
    {'name': 'A', 'ost': 2600100, 'nord': 1200200},
    {'name': 'B', 'ost': 2601500, 'nord': 1201000},
    {'name': 'C', 'ost': 2599800, 'nord': 1199500},
    {'name': 'D', 'ost': 2600800, 'nord': 1200600},
    {'name': 'E', 'ost': 2602000, 'nord': 1198000},
    ]

    bbox = {'ost_min': 2600000, 'ost_max': 2601000,
        'nord_min': 1200000, 'nord_max': 1201000}

    innerhalb = 0
    Ausserhalb = 0

    for punkt in punkte:
        if (bbox['ost_min'] <= punkt['ost'] <= bbox['ost_max'] and
            bbox['nord_min'] <= punkt['nord'] <= bbox['nord_max']):
            print(punkt['name'], "ist in der Box")
            innerhalb += 1
        else:
            print(punkt['name'], "ist nicht in der Box")
            Ausserhalb += 1
        
    print("Innerhalb", innerhalb)
    print("Ausserhalb", Ausserhalb)
    