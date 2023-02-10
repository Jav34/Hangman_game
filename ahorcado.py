import random

def podaj_litere():
    nowa_litera = input("Wpisz kolejną literkę: ")
    if nowa_litera == word_random:
        quit("Zgadłeś słowo. Gratulacje!")
    if nowa_litera in word_lista:
        print("Dobrze! Jest taka literka w słowie!")
    if nowa_litera not in word_lista:
        quit("Ups... nie ma takiej literki :(")

words = ['życie', 'kot', 'pies', 'kredka', 'masło', 'telefon', 'jabłko', 'pytanie', 'nuda', 'szkoła',
         'kartkówka', 'słowo', 'sto', 'tramwaj', 'gra', 'szklanka', 'kasa', 'miłość', 'długopis', 'kalkulator',
         'koszyk', 'paznokcie', 'bluzka', 'spodnie', 'kropka', 'koń', 'gruszka', 'chipsy', 'pudełko', 'herbata',
         'dziewczyna', 'polska', 'ziemia', 'oceny', 'szczoteczka', 'wanna', 'gąbka', 'serce', 'łyżka', 'frytki',
         'cenzura', 'butelka', 'woda', 'spodnie', 'nogi', 'basen', 'makaron', 'kleszcz', 'smutek', 'radość',
         'rozum', 'emocje', 'młodzież', 'zeszyt', 'samochód', 'chomik', 'piasek', 'kamień', 'oczy', 'uszy',
         'ręcznik', 'ręce', 'internet', 'śliwka', 'książka', 'ołówek', 'taniec', 'igła', 'ogień', 'ludzie',
         'świat', 'włosy', 'mydło', 'klawiatura', 'komputer', 'ekran', 'monitor', 'ogon', 'łza', 'metka',
         'sklep', 'praca', 'małpa', 'zoo', 'wojna', 'historia', 'pytanie', 'gra', 'ubrania', 'szafka',
         'worek', 'kabel', 'ładowarka', 'zegar', 'czas', 'uśmiech', 'urodziny', 'kwiaty', 'przyroda', 'kartka',
         'zajączek', 'wielkanoc', 'piątek', 'niedziela', 'plecak', 'globus', 'magia', 'przyjaźń', 'piłka'
         ]
word_random = random.choice(words)
word_length = len(word_random)
word_lista = list(word_random)

if word_length <= 4:
    print("Wylosowane słowo ma:", word_length, "literki. \nPierwsza literka to: ", word_random[0].upper())
else:
    print("Wylosowane słowo ma:", word_length, "literek. \nPierwsza literka to: ", word_random[0].upper(),
          "\nA ostatnia to: ", word_random[-1].upper())

for w in word_random:
    w.replace(word_random, '*')
    print(w)

for word in range(2, word_length):
    podaj_litere()
