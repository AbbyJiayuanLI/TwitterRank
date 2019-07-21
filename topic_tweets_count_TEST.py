import networkx as nx
import twint


f = open('./data/network_TEST_DONE.txt', 'r')
# f = open('./data/network_PREDICT_DONE.txt', 'r')
userDict = eval(f.read())
userGraph = nx.DiGraph(userDict)

userList = list(userGraph.nodes)

# NEED TO CHANGE
userList = [userList[i] for i in range(0, 100)]
userList.sort()

topic_tweet_Dict = {}

userCount = 0
for user in userList:
    
    print(user)
    c = twint.Config()
    c.Username = user
    c.Store_object = True
    c.Search = "movie OR cinema OR film OR theater"
    twint.run.Search(c)

    tweets_count = len(twint.output.tweets_list)
    topic_tweet_Dict[user] = tweets_count

    print()
    print()
    print()
    print()
    print(topic_tweet_Dict)

    # clear the list
    twint.output.tweets_list = []

    if (userCount % 5 == 0) and (userCount > 0):
        output_topicNumber = open('user_Topic_tweet_Count_TEST.txt', 'w')
        # output_topic_tweet_count = open('user_Topic_tweet_Count_PREDICT.txt', 'w')
        userTopic_tweet_Dict_str = str(topic_tweet_Dict)
        output_topic_tweet_count.write(userTopic_tweet_Dict_str)
        output_topic_tweet_count.close()

if (userCount % 5 == 0) and (userCount > 0):
    output_topicNumber = open('user_Topic_tweet_Count_TEST.txt', 'w')
    # output_topic_tweet_count = open('user_Topic_tweet_Count_PREDICT.txt', 'w')
    userTopic_tweet_Dict_str = str(topic_tweet_Dict)
    output_topic_tweet_count.write(userTopic_tweet_Dict_str)
    output_topic_tweet_count.close()




    






