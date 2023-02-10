# Word Counter Function
def word_counter():
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
    # for key, val in counts.items():
    #     newtup = (val, key)
    #     lst.append(newtup)
    # list = sorted(lst, reverse=True)

    list = sorted([(v,k) for k,v in counts.items()], reverse = True)

    for val,key in list[:10]:
        print(key, val)
    # Create Output
    print(f"Word Most Used: {list[0][1]}")
    print(f"Word Count: {list[0][0]}")
# Call Function
word_counter()
