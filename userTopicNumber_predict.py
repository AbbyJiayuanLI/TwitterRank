import networkx as nx
import twint


# f = open('./testUserDONE.txt', 'r')
f = open('./predictUserDONE.txt', 'r')
userDict = eval(f.read())
userGraph = nx.DiGraph(userDict)

userList = list(userGraph.nodes)

userList = [userList[i] for i in range(0, 100)]
userList.sort()

userTopicDict = {}

userCount = 0
for user in userList:
    
    print(user)
    c = twint.Config()
    c.Username = user
    c.Store_object = True
    c.Search = "movie OR cinema OR film OR theater"
    twint.run.Search(c)

    count = 0
    for tweet in twint.output.tweets_list:
        tweet = str(tweet.tweet)
        count += tweet.count('movie') + tweet.count('film') + tweet.count('theater') + tweet.count('cinema')

    userTopicDict[user] = count

    if (userCount % 5 == 0) and (userCount > 0):
        output = open('userTopicCount.txt', 'w')
        userTopicDict_str = str(userTopicDict)
        output.write(userTopicDict_str)
        output.close()

output = open('userTopicCount.txt', 'w')
userTopicDict_str = str(userTopicDict)
output.write(userTopicDict_str)
output.close()




    






