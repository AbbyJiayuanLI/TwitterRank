import csv

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
topic_keyword_count_TEST = dictSort(eval(open('./data/topic_number_dict_TEST.txt', 'r').read()))
topic_keyword_count_PREDICT = dictSort(eval(open('./data/topic_number_dict_PREDICT.txt', 'r').read()))


print(retweet_dict_PREDICT)

out_retweet_dict_TEST = export('retweet_count_TEST.csv', retweet_dict_TEST)
out_retweet_dict_PREDICT = export('retweet_count_PREDICT.csv', retweet_dict_PREDICT)
out_TopicCount_dict_TEST = export('tweets_keyword_count_TEST.csv', topic_keyword_count_TEST) 
out_TopicCount_dict_PREDICT = export('tweets_keyword_count_PREDICT.csv', topic_keyword_count_PREDICT) 
out_topic_tweets_count_TEST = export('topic_tweets_count_TEST.csv', topic_tweets_count_TEST)
out_topic_tweets_count_PREDICT = export('topic_tweets_count_PREDICT.csv', topic_tweets_count_PREDICT)
