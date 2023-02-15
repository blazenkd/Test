# 2/13/2023
"""
" How do I organize this test file?
What is its purpose?

"""
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

    # Simpler way of doing program using list comprehension
    list = sorted([(v,k) for (k,v) in counts.items()], reverse = True)
    print(f"Top 5 most used words: ")
    for (val,key) in list[:5]:
        print(key, val)
    # Switch the key, value pairs
    list_5 = [(key,val) for (val,key) in list[:5]]
    print(list_5)
    # Create Output
    print(f"Word Most Used: {list[0][1]}")
    print(f"Word Count: {list[0][0]}")

    # Return an output
    return list_5

# Call Function Variable
top_words = count_words()
