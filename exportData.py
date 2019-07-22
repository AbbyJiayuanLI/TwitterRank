import csv
import networkx as nx

def export(filename, list1):
    with open(filename, mode = 'w') as csv_file:
        writer = csv.writer(csv_file)
        for i in list1:
            writer.writerow(i)

def dictSort(dict1):
    dict1 = sorted(dict1.items(), key = lambda x: x[0])
    return dict1


retweet_dict_TEST = dictSort(eval(open('./data/retweet_dict_TEST.txt', 'r').read()))
retweet_dict_PREDICT = dictSort(eval(open('./data/retweet_dict_PREDICT.txt', 'r').read()))
topic_tweets_count_TEST = dictSort(eval(open('./data/topic_tweets_dict_TEST.txt', 'r').read()))
topic_tweets_count_PREDICT = dictSort(eval(open('./data/topic_tweets_dict_PREDICT.txt', 'r').read()))
topic_keyword_count_TEST = dictSort(eval(open('./data/topic_keyword_dict_TEST.txt', 'r').read()))
topic_keyword_count_PREDICT = dictSort(eval(open('./data/topic_keyword_dict_PREDICT.txt', 'r').read()))
user_tweets_count_TEST = dictSort(eval(open('./data/userTweetsCount_TEST.txt', 'r').read()))
user_tweets_count_PREDICT = dictSort(eval(open('./data/userTweetsCount_PREDICT.txt', 'r').read()))

for i in user_tweets_count_TEST:
    flag = 0
    for j in topic_keyword_count_TEST:
        if i[0] != j[0]:
            flag = 1
        # 0 means i[0] is common element
        else:
            flag = 0
            break
    # 1 means not common
    if flag == 1:
        for m in topic_keyword_count_TEST:
            if m[0] == i[0]:
                topic_keyword_count_TEST.remove(m)
        for m in topic_tweets_count_TEST:
            if m[0] == i[0]:
                topic_tweets_count_TEST.remove(m)
        for m in retweet_dict_TEST:
            if m[0] == i[0]:
                retweet_dict_TEST.remove(m)

for i in user_tweets_count_PREDICT:
    flag = 0
    for j in topic_keyword_count_PREDICT:
        if i[0] != j[0]:
            flag = 1
        # 0 means i[0] is common element
        else:
            flag = 0
            break
    # 1 means not common
    if flag == 1:
        for m in topic_keyword_count_PREDICT:
            if m[0] == i[0]:
                topic_keyword_count_PREDICT.remove(m)
        for m in topic_tweets_count_PREDICT:
            if m[0] == i[0]:
                topic_tweets_count_PREDICT.remove(m)
        for m in retweet_dict_PREDICT:
            if m[0] == i[0]:
                retweet_dict_PREDICT.remove(m)

out_retweet_dict_TEST = export('retweet_count_TEST.csv', retweet_dict_TEST)
out_retweet_dict_PREDICT = export('retweet_count_PREDICT.csv', retweet_dict_PREDICT)
out_TopicCount_dict_TEST = export('tweets_keyword_count_TEST.csv', topic_keyword_count_TEST) 
out_TopicCount_dict_PREDICT = export('tweets_keyword_count_PREDICT.csv', topic_keyword_count_PREDICT) 
out_topic_tweets_count_TEST = export('topic_tweets_count_TEST.csv', topic_tweets_count_TEST)
out_topic_tweets_count_PREDICT = export('topic_tweets_count_PREDICT.csv', topic_tweets_count_PREDICT)
out_user_tweets_count_TEST = export('user_tweets_count_TEST.csv', user_tweets_count_TEST)
out_user_tweets_count_PREDICT = export('user_tweets_count_PREDICT.csv', user_tweets_count_PREDICT)

network_dict_TEST = eval(open('./data/network_TEST_DONE.txt', 'r').read())
network_dict_PREDICT = eval(open('./data/network_PREDICT_DONE.txt', 'r').read())

network_TEST = nx.DiGraph(network_dict_TEST)
network_PREDICT = nx.DiGraph(network_dict_PREDICT)

print(network_TEST.nodes)
print(len(network_TEST.nodes))
print(len(user_tweets_count_TEST))

for i in user_tweets_count_TEST:
    flag = 0
    for j in network_TEST.nodes:
        if j != i[0]:
            flag = 1
        else:
            flag = 0
    if flag == 1:
        network_TEST.remove_node(i[0])


for i in user_tweets_count_PREDICT:
    flag = 0
    for j in network_PREDICT.nodes:
        if j != i[0]:
            flag = 1
        else:
            flag = 0
    if flag == 1:
        network_PREDICT.remove_node(i[0])


out_network_TEST = open('./data/network_TEST_DONE1.txt', 'w')
out_network_PREDICT = open('./data/network_PREDICT_DONE1.txt', 'w')
out_network_TEST.write(str(nx.to_dict_of_dicts(network_TEST)))
out_network_PREDICT.write(str(nx.to_dict_of_dicts(network_PREDICT)))
out_network_TEST.close()
out_network_PREDICT.close()




