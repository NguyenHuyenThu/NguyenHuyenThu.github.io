from collections import Counter

words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under'
]

word_counts  = Counter(words)

top_three = word_counts.most_common(3)

print(top_three) # [('eyes', 8), ('the', 5), ('look', 4)]

def counter(items):
    dic = dict()
    for item in items:
        if item not in dic:
            dic[item] = 1
        else:
            dic[item] += 1
    return dic

a = ['aa','cc','aa']

print(counter(a))