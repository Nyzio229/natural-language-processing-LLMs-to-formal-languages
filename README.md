# natural-language-processing-LLMs-to-formal-languages
# Projekt badawczy: Transformacja i dostosowanie modelu językowego przetwarzającego język naturalny do rozumienia i obsługiwania języków formalnych

## Opis projektu

Repozytorium zawiera komplet materiałów badawczych powstałych w ramach projektu badawczego, którego celem była **analiza zachowania przeszkolonych modeli językowych** oraz **próba rekonstrukcji ich wewnętrznych struktur decyzyjnych** za pomocą algorytmu **L\*** (Angluin).

Projekt stanowi **bazę empiryczną i metodologiczną** do przygotowania pracy magisterskiej z zakresu:
- uczenia maszynowego,
- modeli językowych (LLM),
- inferencji automatów,
- formalnej analizy zachowania modeli AI.

## Cele badawcze

Główne cele projektu:
- przeszkolenie kilku wariantów modeli językowych,
- ocena ich deterministyczności i stabilności odpowiedzi,
- analiza wpływu parametrów inferencji na wyniki,
- zastosowanie algorytmu **L\*** do inferencji automatów,
- wizualizacja uzyskanych automatów i analiza ich struktury.

## Zakres badań

Projekt obejmuje:
- **8 przeszkolonych modeli językowych**,
- testy odpowiedzi na ustalone zestawy zapytań,
- analizę powtarzalności wyników,
- integrację modeli z algorytmem L\*,
- generowanie automatów deterministycznych (DFA).

## Zastosowane metody i technologie

### Metody badawcze
- fine-tuning modeli językowych (LoRA),
- testy deterministyczności,
- inferencja automatów (L\*),
- analiza strukturalna automatów.

### Technologie
- Python 3.x  
- PyTorch  
- HuggingFace Transformers  
- LoRA / PEFT  
- Ollama  
- Graphviz / NetworkX  

## Trenowanie modeli

Proces trenowania obejmował:
1. wybór bazowego modelu językowego,
2. przygotowanie danych,
3. fine-tuning metodą **LoRA**,
4. eksport modeli do `.gguf`,
5. testy inferencji lokalnej.

## Testy i wyniki

Analiza obejmuje:
- deterministyczność odpowiedzi,
- wpływ parametrów inferencji,
- strukturę automatów,
- porównanie modeli.

## Algorytm L*

Modele zostały użyte jako **oracle** dla algorytmu L\*, co pozwoliło na:
- rekonstrukcję automatów,
- analizę złożoności zachowania,
- porównanie modeli.

## Struktura repozytorium

```
.
├── data/
├── models/
├── notebooks/
├── lstar/
├── results/
├── visualizations/
├── report/
└── README.md
```

## Wnioski

- deterministyczność modeli LLM jest ograniczona,
- algorytm L\* pozwala na uchwycenie uproszczonych wzorców decyzyjnych,
- struktura automatów różni się między modelami.


## Autor

Autor: **[Norbert Jaskulski]**  
Uczelnia: UMK w Toruniu
