import twint
import networkx as nx



# f = open('testUsers.txt', 'r')
f = open('predictUser.txt', 'r')

userStr = f.read()

userDict = eval(userStr)

userGraph = nx.DiGraph(userDict)

print("Nodes number: %d" % (userGraph.number_of_nodes()))
print("Edges number: %d" % (userGraph.number_of_edges()))

userList = set(userGraph.nodes)

count = 0
for user in userList:
    c = twint.Config()
    c.Username = user
    c.Store_object = True
    c.Limit = 100
    print("user: %s 's follower" % (user))
    twint.run.Followers(c)

    count += 100

    followers = twint.output.follows_list
    followers = set(followers)
    overlap = followers & userList
    for i in overlap:
        userGraph.add_edge(i, user)

    twint.output.follows_list = []

    if count == 1000:
        output = nx.to_dict_of_dicts(userGraph)
        strOutput = str(output)
        f = open('PredictUserDONE.txt', 'w')
        f.write(strOutput)
        f.close()
        print("File saved")
        print("count : %d" %(count))

    if count % 1000 == 0 and count > 1000:
        output = nx.to_dict_of_dicts(userGraph)
        strOutput = str(output)
        f = open('PredictUserDONE.txt', 'w')
        f.write(strOutput)
        f.close()
        print("File saved")
        print("count : %d" %(count))
    #         break
    # break

print("add Complete")

output = nx.to_dict_of_dicts(userGraph)
strOutput = str(output)
f = open('PredictUserDONE.txt', 'w')
f.write(strOutput)
f.close()

print("save complete")

print(list(userGraph.edges))

