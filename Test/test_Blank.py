
"""
2/10/2023 
Time: 10 min 47 sec
2/11/2023
Time: 7 min 39 sec
Mistakes:
    None
Slow:
lst = sorted([(v,k) for (k,v) in counts.items()], reverse = True)
print(f"Top 5 Most Common Words: ")
for (k,v) in lst[:5]
    print((k,v))
print(f"Most Common Word: {lst[0][1]}")
print(f"Most Common Word Count: {lst[0][0]}")
"""

# Iteration 1
def count_words():
    name = input("Enter File Name: ")
    handle = open(name)

    counts = dict()
    for line in handle:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1

    lst = sorted([(v,k) for (k,v) in counts.items()], reverse=True)
    print(f"Top 5 Most Common Words: ")
    for k,v in lst[:5]:
        print((k,v))

    print(f"Most Common Word: {lst[0][1]}")
    print(f"Most Common Word Count: {lst[0][0]}")
count_words()
