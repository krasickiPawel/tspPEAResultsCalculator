import sys


def calculate(measurementList, bestResult):
    finalResultList = []
    for measurement in measurementList:                                                 # obliczamy błąd względny
        finalResultList.append((abs(measurement - bestResult) / bestResult) * 100)      # wyrażony w procentach
    return finalResultList                                                              # i zwracamy listę błędów względnych


def fileRead(fileName):
    with open(fileName) as file:
        data = file.readlines()                             # odczyt linijek pliku i dodanie każdej do listy
    data = [int(result.strip().removesuffix('\n')) for result in data if result != "" and result != '\n']   # odfiltrowanie błędnych danych wejściowych w postaci pustych linijek
    return data                                             # zwrot przygotowanych odczytanych danych


def fileSave(data, fileToSave):                             # zapis do pliku
    with open(fileToSave, 'w') as file:
        for d in data:
            d *= 10
            d = round(d)                                    # zaokrąglenie wyniku do 1 liczby po przecinku
            d /= 10
            d = str(d)                                      # zamiana wyniku na string aby upiekszyc wyniki (. -> ,)
            d = d.replace(".", ",")                         # zamiana kropek na przecinki w celu pokazania wartosci dziesietnych
            file.write(d + "\n")                            # zapis błędu względnego wyrażonego w procentach z przejściem do nowej linii


def doEverything(fileName, fileToSave, bestSolution):       # wrapper przyjmujący wartości i robiący to co program ma robić
    fileSave(calculate(fileRead(fileName), bestSolution), fileToSave)


if __name__ == '__main__':
    if len(sys.argv) == 4:                                  # podstawowe zabezpieczenie czy podano wymaganą ilość parametrów
        try:
            fileToRead = sys.argv[1]                        # plik z danymi wejściowymi
            fileToSave = sys.argv[2]                        # plik z danymi wyjściowymi
            bestSolution = int(sys.argv[3])                 # najlepsze znane rozwiązanie dla badanego rozmiaru tsp
            doEverything(fileToRead, fileToSave, bestSolution)
        except FileNotFoundError:                           # inne wyjątki to już wypisze nam interpreter bo mogą być różne
            print("Podany do odczytu plik nie istnieje")    # jeśli ktoś na siłę będzie chciał "zepsuć" program
    else:
        print("Podaj poprawną ilość argumentów")
