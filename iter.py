class iterates:
    def __init__(self):
        self.nums = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.nums <= 5:
            value = self.nums
            self.nums += 1
            return value
        else:
            raise StopIteration


ok = iterates()
for i in ok:
    print(i)


# nums = [8, 5, 6, 9]

# it = iter(nums)

# print(it.__next__())
# print(it.__next__())
