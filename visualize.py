import networkx as nx

#import
userDict = eval(open('./network_PREDICT_DONE.txt', 'r').read())
userGraph = nx.DiGraph(userDict)


