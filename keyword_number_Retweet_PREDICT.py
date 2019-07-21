import networkx as nx
import twint


# f = open('./network_TEST_DONE.txt', 'r')
f = open('./network_PREDICT_DONE.txt', 'r')
userDict = eval(f.read())
userGraph = nx.DiGraph(userDict)

userList = list(userGraph.nodes)

# NEED TO CHANGE
userList = [userList[i] for i in range(0, 100)]
userList.sort()

userTopicDict = {}
userRetweetDict = {}

userCount = 0
for user in userList:
    
    print(user)
    c = twint.Config()
    c.Username = user
    c.Store_object = True
    c.Search = "movie OR cinema OR film OR theater"
    twint.run.Search(c)

    Topic_count = 0
    retweetCount = 0
    for tweet in twint.output.tweets_list:
        tweet_str = str(tweet.tweet)
        retweetCount += int(tweet.retweets_count)
        Topic_count += tweet_str.count('movie') + tweet_str.count('film') + tweet_str.count('theater') + tweet_str.count('cinema')

    userTopicDict[user] = Topic_count
    userRetweetDict[user] = retweetCount

    print(userTopicDict)
    print(userRetweetDict)

    # clear the list
    twint.output.tweets_list = []

    if (userCount % 5 == 0) and (userCount > 0):
        # output_topicNumber = open('userTopicCount_TEST.txt', 'w')
        output_topicNumber = open('user_TopicCount_PREDICT.txt', 'w')
        userTopicDict_str = str(userTopicDict)
        output_topicNumber.write(userTopicDict_str)
        output_topicNumber.close()

        # NEED TO CHANGE
        # output_retweet = open('userretweet_TEST.txt', 'w')
        output_retweet = open('user_retweet_PREDICT.txt', 'w')
        user_retweetDict_str = str(userRetweetDict)
        output_retweet.write(user_retweetDict_str)
        output_retweet.close()


# NEED TO CHANGE
# output_topicNumber = open('userTopicCount_TEST.txt', 'w')
output_topicNumber = open('userTopicCount_PREDICT.txt', 'w')
userTopicDict_str = str(userTopicDict)
output_topicNumber.write(userTopicDict_str)
output_topicNumber.close()

# NEED TO CHANGE
# output_retweet = open('userretweet_TEST.txt', 'w')
output_retweet = open('user_retweet_PREDICT.txt', 'w')
user_retweetDict_str = str(userRetweetDict)
output_retweet.write(user_retweetDict_str)
output_retweet.close()


    






