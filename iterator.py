# Iterate Python dictionary keys

d = {'name': 'Alice', 'age': 23, 'country': 'NL' }
for k in d:
    print(k)
# Iterate dictionary values
for k in d.values():
    print(k)

# Iterate dictionary keys and values

for k,v in d.items():
    print(k, v)

# Creating your own Python iterator
class EvenNumbers:
    last = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.last += 2
        if self.last > 8:
            raise StopIteration
        return self.last
even_numbers = EvenNumbers()
for num in even_numbers:
    print(num)