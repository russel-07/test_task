# Тестовое задание

## Вопрос №1
На языке Python написать алгоритм (функцию) определения четности целого числа, который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути. Объяснить плюсы и минусы обеих реализаций. 
  
Пример:
```python
def isEven(value):
      return value % 2 == 0
```
  
При представлении числа в двоичной системе счисления, младший разряд
является признаком четности/нечетности числа. В предложенном мной алгоритме
используется операция логического умножения, на заданное число накладывается
маска, которая определяет значение младшего разряда и в соответсвии с ним
возвращает ответ.
Данный алгоритм работает быстрее, чем алгоритм предложенный в задании, т.к.
операция деления дороже, чем операция умножения.  

## Вопрос №2
На языке Python написать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.
  
Для реализации циклического буфера FIFO мной предложено два класса:
- Первая реализация очереди основана на массиве.
Элементы очереди хранятся в последовательных ячейках
памяти, что ускоряет доступ к данным. Сложность добавления,
извлечения и поиска элемента в данной реализации составляет O(1).
Недостатком данной реализации является ограничение максимального размера
очереди.
- Вторая реализация очереди использует связный список.
В данной реализации нет ограничения на максимальный размер очереди.
Элементы очереди хранятся в произвольных ячейках памяти, что замедляет
итерацию по элементам, а также требуется выделение дополнительной памяти
для хранения указателей.
Сложность операций добавления и извлечения элемента из очереди составляет
O(1), сложность поиска элемента в очереди в худшем случае составляет O(n).  


## Вопрос №3
На языке Python предложить алгоритм, который быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел. Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным). Объяснить, почему вы считаете, что функция соответствует заданным критериям.
  
Для реализации сортировки использован алгоритм сортировки
слиянием. Сложность данного алгоритма сосотавлет O(n log n).
Алгоритм сортировки, основанный на сравнении элементов между собой
невозможно созадть со сложностью менее чем O(n log n), что доказывается
математически.
Есть алгоритмы сортировки, основанные на других принципах и могут работать
быстрее, например поразрядная сортировка, сортировка подсчетом,
но в данной задаче, при определенных входных данных, такие алгоритмы
будут работать медленнее, а сортировка слиянием всегда будет работать за
O(n log n).
