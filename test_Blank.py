
"""
2/10/2023 
Time: 10 min 47 sec
Mistakes:
    handle = open(name)
    list = sorted([(v,k) for k,v in counts.items()], reverse = True)
    print(f"Top 10 words: ")
    for v,k in list[:10]:
        print(k,v)
"""

def word_counter():
    name = input("Enter File Name: ")
    handle = open(name)

    counts = dict()
    for line in handle:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1

    list = sorted([(v, k) for k,v in counts.items()], reverse=True)
    print(f"Top 10 words: ")
    for v,k in list[:10]:
        print(k,v)  

    print(f"Most used word: {list[0][1]}")
    print(f"Word Count: {list[0][0]}")

word_counter()