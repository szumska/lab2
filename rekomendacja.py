from math import sqrt

users = {"Ania": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bonia":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Celina": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dominika": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Ela": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Fruzia":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Gosia": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Hela": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }



def manhattan(rating1, rating2):
    #Oblicz odległość w metryce taksówkowej miedzy dwoma  zbiorami ocen
    # danymi w postaci: {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}
    #Zwróć -1, gdy zbiory nie mają wspólnych elementów

    klucz1=rating1.keys()
    klucz2=rating2.keys()
    odleglosc=0
    odlegloscodwszystkich=0
    porownanie=False

    for klucz in klucz1:
        if klucz in rating2.keys():
            porownanie=True
            odlegloscodwszystkich=odlegloscodwszystkich+abs(rating2[klucz]-rating1[klucz])
        if porownanie==True:
            return odlegloscodwszystkich
        else:
            return -1
    pass


def computeNearestNeighbor(username, users):
    #dla danego użytkownika username, zwróć ze słownika users nazwę użytkownika o najbliższych preferencjach"""

    nameOfNearestNeighbor=""
    odleglosci = []
    username2 =""

    for username2 in users:
        if username2!=username:
            odleglosc=0
            odleglosc=manhattan(users[username],users[username2])
            odleglosci.append((odleglosc, username2))
    return sorted(odleglosci)

    nameOfNearestNeighbor=sorted(odleglosci)
    print(nameOfNearestNeighbor[1])
    return nameOfNearestNeighbor[1]

recommendations=[]

def recommend(username, users):
    #Zwróć listę rekomendacji dla użytkownika
    # znajdź preferencje najbliższego sąsiada

    nearestName = computeNearestNeighbor(username, users)[0][1]
    print('Najblizszy sasiad to: %s' % nearestName)

    # zarekomenduj użytkownikowi wykonawcę, którego jeszcze nie ocenił, a zrobił to jego najbliższy sąsiad

    ratingOfNearest=users[nearestName]
    print('Rekomendaje uzytkownika: ')
    print(ratingOfNearest)

    userRating=users[username]

    for artists in ratingOfNearest:
        if not artists in userRating:
            recommendations.append((artists,ratingOfNearest[artists]))
    
    return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True)


print(recommend('Bonia', users))
