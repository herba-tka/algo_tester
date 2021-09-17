# Szkielet Projektu `algo_tester` 
`algo_tester` to aplikacja do testowania programów
przyjmuje nazwę programu, plik wejściowy i plik wyjściowy

1. Uruchamia program
2. Podaje dane wejściowe
3. Sprawdza czy dane wyjściowe się zgadzają i czy nie wystąpił błąd
4. Wypisuje wynik


## Przykład użycia:

Mamy program `greeter.py` który chcemy przetestować dla danych wejściowych z plików 1.in i  2.in.
Podane są spodziewane dane wyjścia w plikach 1.out i 2.out.

### Przykład nie działającego testu
```
./algo_tester.py greeter.py 1.in 1.out

```


### Przykład działającego testu:

```
./algo_tester.py greeter.py 2.in 2.out

```

