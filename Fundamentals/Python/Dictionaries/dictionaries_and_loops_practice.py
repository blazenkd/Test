# Word Counter Function
def word_counter(name):
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
word_counter("word.txt")


# ---Practice building that function---

# Create Function Name
def word_counter_1(name):
    # Create Input
    name = input("Enter file name: ")
    handle = open(name)
    # Construct Dictionary
    counts = dict()
    for lines in handle:
        words = lines.split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1
    # Create Logic for word count
    bigCount = None
    bigWord = None
    for (key, value) in counts.items():
        if bigCount is None or bigCount < value:
            bigCount = value
            bigWord = key
    # Create Output
    print(f"Word Most Used: {bigWord}")
    print(f"Word Count: {bigCount}")
# Call Function


