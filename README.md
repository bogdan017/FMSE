# Factorizare cu algoritmul lui Shor

Acest proiect demonstrează implementarea și utilizarea **algoritmului lui Shor** pentru factorizarea numerelor întregi folosind Qiskit **0.42.1** și simulatorul local Aer. 

## Obiective

- Ilustrarea avantajului exponențial al calculului cuantic în fața celui clasic.  
- Demonstrarea pașilor algoritmului lui Shor: alegerea numărului _r_, estimarea cuantică a perioadei, calculul factorilor primi.  

## Compatibilitate și limitări

Începând cu **Qiskit Terra 0.25.0**, pachetul este considerat „end-of-life” pentru algoritmii clasici de factorizare, iar implementarea `Shor` a fost eliminată din versiunile care rulează pe hardware-ul IBM Q. Prin urmare, **testarea algoritmului lui Shor pe o maşină IBM Q reală nu mai este posibilă** în noile versiuni. Singura opţiune practică rămâne **simularea locală** cu Aer, utilizând versiunile anterioare de Qiskit:

```text
qiskit              0.42.1
qiskit-terra        0.23.3   # ultimele versiuni compatibile cu Shor (algoritmul este considerat deprecated din versiunea 0.22.0)
qiskit-aer          0.12.0
qiskit-ibm-provider 0.5.0    # doar pentru configurări de backend, nu pentru aplicarea algoritmului lui Shor pe hardware
```

Importurile necesare pentru rularea codului sunt: 
from qiskit import Aer
from qiskit.algorithms import Shor
from qiskit.utils import QuantumInstance

iar algoritmul propriu zis este următorul:

backend = Aer.get_backend("aer_simulator")
qi = QuantumInstance(backend, shots=1024)
shor = Shor(quantum_instance=qi)
N=21
result = shor.factor(N)
print("Factorii lui",N, "sunt:", result.factors)

O simpla rulare în consolă a fisierului ce conține algoritmul, cu comanda **python3 quantum_factorization.py** va avea următorul rezultat:

The Shor class is deprecated as of Qiskit Terra 0.22.0 and will be removed ...

Factorii lui 21 sunt: [[3, 7]]

Warning-ul afișat este legat de compatibilitatea discutată anterior, algoritmul fiind eliminat din versiunile noi de Qiskit ≥ 1.0.
