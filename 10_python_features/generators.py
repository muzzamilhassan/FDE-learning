# In JS: function* countUp() { yield 1; yield 2; }
# In Python: Any function with 'yield' is a generator (lazy, memory-efficient)

def count_up(limit: int):
    n = 1
    while n <= limit:
        yield n
        n += 1

gen = count_up(3)
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
