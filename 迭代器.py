def fac(n):
    k = []
    for i in range(n):
        k.append(i)
    return k


a = fac(10)
print(a)


def fac(n):
    for i in range(n):
        yield i


a = fac(10)
print(a.__next__())


class Sequencelterator:
    def __init__(self, sequence):
        self._seq = sequence
        self._k = -1

    def __next__(self):
        self._k += 1
        if self._k < len(self._seq):
            return self._seq[self._k]

    def __iter__(self):
        return self


a = Sequencelterator('adafsdfasdf')
# print(a.__next__())
# print(a.__next__())
for i in range(len(a._seq)):
    print(a.__next__())


# 自定义range类
# range是是一个循环遍历的函数
class Range:
    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError('step cannot be 0')
        if stop is None:
            start, stop = 0, start
        self._length = max(0, (stop - start + step - 1) // step)
        self._start = start
        self._step = step

    def __len__(self):
        return self._length

    def __getitem__(self, k):
        if k < 0:
            k += len(self)

        if not 0 <= k < self._length:
            raise IndexError('index out of range')

        return self._start


class Animal:


    def __init__(self, animal_list):
        self.animals_name = animal_list


    def __getitem__(self, index):
        return self.animals_name[index]


animals = Animal(["dog", "cat", "fish"])
for animal in animals:
    print(animal)
