# Word Counter Function
def count_words():
    # Create Input
    name = input('Enter name file:')
    handle = open(name)
    # Construct Dictionary
    counts = dict()
    for line in handle:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1

    # Create Logic for word count
    lst = []
    for (key, val) in counts.items():
        newtup = (val, key)
        lst.append(newtup)
    lst = sorted(lst, reverse=True)

    # Simpler way of doing program using list comprehension
    list = sorted([(v,k) for (k,v) in counts.items()], reverse = True)

    print(f"Top 10 most used words: ")
    for (val,key) in list[:10]:
        print(key, val)

    # Create Output
    print(f"Word Most Used: {list[0][1]}")
    print(f"Word Count: {list[0][0]}")

# Call Function
count_words()
