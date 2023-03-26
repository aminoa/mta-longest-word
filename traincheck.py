import csv
import networkx as nx
import matplotlib.pyplot as plt
from pygtrie import StringTrie

mta = nx.Graph()

with open('train_stops.csv', 'r') as f:
    next(f)
    reader = csv.reader(f)
    for train_start, train_end, line in reader:
        train_start = train_start[:3]
        train_end = train_end[:3]

        if train_start not in mta:
            mta.add_node(train_start)
        if train_end not in mta:
            mta.add_node(train_end)

        mta.add_edge(train_start, train_end, line=line)

# nx.draw(mta, with_labels=True)
# plt.show()
# plt.savefig("filename.png")

t_words = StringTrie()
with open('valid_words.txt', 'r') as f:
    file_words = f.read().splitlines()
    for word in file_words:
        # print(word)
        if word:
            t_words[str(word)] = True


# TODO: find the longest word in the trie that is also a valid path in the graph

