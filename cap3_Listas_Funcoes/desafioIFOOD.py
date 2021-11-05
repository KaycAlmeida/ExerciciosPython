#Enterprise Connection – Fase 2
from operator import itemgetter

restaurante = [["Lamen Kazu", 4.8, 0.7],
               ["Mr. Pretzels", 4.7, 1.1],
               ["We Coffee", 4.5, 0.8],
               ["Brigaderia", 4.7, 1.2],
               ["Amor aos Pedaços", 4.3, 1.2],
               ["O Mineiro", 4.3, 1.7]]

restaurante.sort(key=itemgetter(1), reverse = True)
print(restaurante)