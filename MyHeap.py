"""Efektywna implementacja algorytmu Djikstry wymaga specyficznej implementacji
    kolejki priorytetowej z możliwością zmniejszania wartości klucza dla elementów oczekujących w kolejce.
    W tym celu stworzona została klasa MyHeap"""

class MyHeap:
    """
    Kopce binarne z dodatkami - zawierać będą elementy będące parą - (wartość, klucz)
    Równolegle będzie trzymany słownik miejsc kluczy w kopcu
    """

    # konstruktor klasy
    def __init__(self):
        self._heap = []
        self._heapsize = 0
        self._place = {}

    # obowiązkowe metody
    def __repr__(self):
        return str(self)

    def __str__(self):
        if self._heapsize > 0:
            return str([self._heap[idx] for idx in range(self._heapsize)])
        else:
            return str([])

    def __len__(self):
        return self._heapsize

    # narzędzia
    def _left(self, idx):
        return 2*idx+1

    def _right(self, idx):
        return 2*idx+2

    def _parent(self, idx):
        return (idx-1)//2

    # pomocnicza funkcja do usuwania elementów - element z góry idzie na swoje miejsce
    def _heapify(self, idx):
        item = self._heap[idx]
        left = self._left(idx)
        while left < self._heapsize:
            # s ma być indeksem mniejszego z synów i-tego elementu
            if left + 1 == self._heapsize:
                s = left
            elif self._heap[left] <= self._heap[left+1]:
                s = left
            else:
                s = left + 1
            if item <= self._heap[s]:
                break
            else:
                self._heap[idx] = self._heap[s]
                (val, key) = self._heap[idx]
                self._place[key] = idx
                idx = s
                left = self._left(idx)
        self._heap[idx] = item
        (val, key) = item
        self._place[key] = idx

    # zmniejszenie wartości - całość
    def decrease_key(self, idx, item):
        while idx > 0 and item < self._heap[self._parent(idx)]:
            self._heap[idx] = self._heap[self._parent(idx)]
            (val, key) = self._heap[idx]
            self._place[key] = idx
            idx = self._parent(idx)
        self._heap[idx] = item
        (val, key) = item
        self._place[key] = idx

    # zmniejszenie wartości - ze znalezieniem obiektu
    def decrease_val(self, key, val):
        item = (val, key)
        if key in self._place:  # jest klucz w kopcu - jeśli nie to nic nie robię
            idx = self._place[key]
            self.decrease_key(idx, item)

    # wyciagnięcie najmniejszego elementu
    def get_min(self):
        minimum = self._heap[0]
        (val, key) = minimum
        del self._place[key]
        self._heapsize -= 1
        if self._heapsize > 0:
            self._heap[0] = self._heap[self._heapsize]
            self._heapify(0)
        return minimum

    # wstawienie nowego elementu
    def insert(self, item):
        if self._heapsize == len(self._heap):
            self._heap.append(item)
        self._heapsize += 1
        self.decrease_key(self._heapsize-1, item)

    # wstawia nowy element (para (wartość klucz)) jeśli klucza nie ma w kopcu
    # jeśli jest, to jeśli nowa wartość jest mniejsza, to poprawia, jeśli nie - to nic nie robi
    def insert_val(self, key, val):
        if key in self._place:
            if (val, key) < self._heap[self._place[key]]:  # jest już w kopcu, jeśli wartość zmniejszona to coś zrobimy
                self.decrease_val(key, val)
        else:
            self.insert((val, key))

"""
#Test działania kopca - sortowanie
kopiec = MyHeap()
for i in range(20):
    kopiec.insert((20-i, 2*i+7))
wynik = []
print(kopiec)
print(kopiec._place)
for i in range(20):
    wynik.append(kopiec.get_min())
#    print(wynik)
#    print(kopiec)
    print(kopiec._place)
print(wynik)
"""

