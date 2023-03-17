# Lesson

# Example
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])

# Methods
print(list(counts))
print(counts.keys())
print(counts.values())
print(counts.items())

# Walk the key/value pairs
for keys,values in counts.items():
    a = keys,values
    print(keys,values)
    print(type(a))


# --- Get a dictionary for a text file ---
name = input('Enter name file:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)

