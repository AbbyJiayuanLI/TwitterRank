import networkx as nx

network_dict_TEST = eval(open('./data/network_TEST_DONE1.txt', 'r').read())
network_dict_PREDICT = eval(open('./data/network_PREDICT_DONE1.txt', 'r').read())

network_TEST = nx.DiGraph(network_dict_TEST)
network_PREDICT = nx.DiGraph(network_dict_PREDICT)


print(len(network_TEST.nodes))
print(len(network_PREDICT.nodes))
