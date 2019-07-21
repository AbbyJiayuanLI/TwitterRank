def merge(dict1, dict2): 
    dict3 = {**dict1, **dict2}
    return dict3

f1 = eval(open('./yanxiao/userretweet_TEST.txt', 'r').read())
f2 = eval(open('./yanxiao/userretweet_TEST1.txt', 'r').read())
f3 = eval(open('./yanxiao/userretweet_TEST2.txt', 'r').read())
f4 = eval(open('./yanxiao/userretweet_TEST3.txt', 'r').read())
f5 = eval(open('./yanxiao/userretweet_TEST4.txt', 'r').read())
f6 = eval(open('./yanxiao/userretweet_TEST5.txt', 'r').read())
f7 = eval(open('./yanxiao/userretweet_TEST6.txt', 'r').read())
f8 = eval(open('./yanxiao/userretweet_TEST7.txt', 'r').read())
f9 = eval(open('./yanxiao/userretweet_TEST8.txt', 'r').read())
f10 = eval(open('./yanxiao/userretweet_TEST9.txt', 'r').read())
f11 = eval(open('./yanxiao/userretweet_TEST10.txt', 'r').read())
f12 = eval(open('./yanxiao/userretweet_TEST11.txt', 'r').read())
f13 = eval(open('./yanxiao/userretweet_TEST12.txt', 'r').read())
f14 = eval(open('./Abby/userretweet_TEST1.txt','r').read())
f15 = eval(open('./Abby/userretweet_TEST2.txt','r').read())
f16 = eval(open('./Abby/userretweet_TEST3.txt','r').read())
f17 = eval(open('./Abby/userretweet_TEST4.txt','r').read())
f18 = eval(open('./Abby/userretweet_TEST5.txt','r').read())
f19 = eval(open('./Abby/userretweet_TEST6.txt','r').read())
f20 = eval(open('./Abby/userretweet_TEST7.txt','r').read())
f21 = eval(open('./Abby/userretweet_TEST8.txt','r').read())
f22 = eval(open('./Abby/userretweet_TEST9.txt','r').read())
f23 = eval(open('./Abby/userretweet_TEST10.txt','r').read())
f24 = eval(open('./Abby/userretweet_TEST11.txt','r').read())
f25 = eval(open('./Abby/userretweet_TEST12.txt','r').read())

g1 = eval(open('./yanxiao/userTopicCount_TEST.txt', 'r').read())
g2 = eval(open('./yanxiao/userTopicCount_TEST1.txt', 'r').read())
g3 = eval(open('./yanxiao/userTopicCount_TEST2.txt', 'r').read())
g4 = eval(open('./yanxiao/userTopicCount_TEST3.txt', 'r').read())
g5 = eval(open('./yanxiao/userTopicCount_TEST4.txt', 'r').read())
g6 = eval(open('./yanxiao/userTopicCount_TEST5.txt', 'r').read())
g7 = eval(open('./yanxiao/userTopicCount_TEST6.txt', 'r').read())
g8 = eval(open('./yanxiao/userTopicCount_TEST7.txt', 'r').read())
g9 = eval(open('./yanxiao/userTopicCount_TEST8.txt', 'r').read())
g10 = eval(open('./yanxiao/userTopicCount_TEST9.txt', 'r').read())
g11 = eval(open('./yanxiao/userTopicCount_TEST10.txt', 'r').read())
g12 = eval(open('./yanxiao/userTopicCount_TEST11.txt', 'r').read())
g13 = eval(open('./yanxiao/userTopicCount_TEST12.txt', 'r').read())
g14 = eval(open('./Abby/userTopicCount_TEST1.txt', 'r').read())
g15 = eval(open('./Abby/userTopicCount_TEST2.txt', 'r').read())
g16 = eval(open('./Abby/userTopicCount_TEST3.txt', 'r').read())
g17 = eval(open('./Abby/userTopicCount_TEST4.txt', 'r').read())
g18 = eval(open('./Abby/userTopicCount_TEST5.txt', 'r').read())
g19 = eval(open('./Abby/userTopicCount_TEST6.txt', 'r').read())
g20 = eval(open('./Abby/userTopicCount_TEST7.txt', 'r').read())
g21 = eval(open('./Abby/userTopicCount_TEST8.txt', 'r').read())
g22 = eval(open('./Abby/userTopicCount_TEST9.txt', 'r').read())
g23 = eval(open('./Abby/userTopicCount_TEST10.txt', 'r').read())
g24 = eval(open('./Abby/userTopicCount_TEST11.txt', 'r').read())
g25 = eval(open('./Abby/userTopicCount_TEST12.txt', 'r').read())

m1 = eval(open('./yanxiao/user_retweet_PREDICT1.txt', 'r').read())
m2 = eval(open('./yanxiao/user_retweet_PREDICT2.txt', 'r').read())
m3 = eval(open('./yanxiao/user_retweet_PREDICT3.txt', 'r').read())
m4 = eval(open('./yanxiao/user_retweet_PREDICT4.txt', 'r').read())
m5 = eval(open('./yanxiao/user_retweet_PREDICT5.txt', 'r').read())
m6 = eval(open('./yanxiao/user_retweet_PREDICT6.txt', 'r').read())
m7 = eval(open('./yanxiao/user_retweet_PREDICT7.txt', 'r').read())
m8 = eval(open('./yanxiao/user_retweet_PREDICT8.txt', 'r').read())
m9 = eval(open('./yanxiao/user_retweet_PREDICT9.txt', 'r').read())
m10 = eval(open('./yanxiao/user_retweet_PREDICT10.txt', 'r').read())
m11 = eval(open('./yanxiao/user_retweet_PREDICT12.txt', 'r').read())
m12 = eval(open('./yanxiao/user_retweet_PREDICT11.txt', 'r').read())
m13 = eval(open('./travis/user_retweet_PREDICT1.txt', 'r').read())
m14 = eval(open('./travis/user_retweet_PREDICT2.txt', 'r').read())
m15 = eval(open('./travis/user_retweet_PREDICT3.txt', 'r').read())
m16 = eval(open('./travis/user_retweet_PREDICT4.txt', 'r').read())
m17 = eval(open('./travis/user_retweet_PREDICT5.txt', 'r').read())
m18 = eval(open('./travis/user_retweet_PREDICT6.txt', 'r').read())
m19 = eval(open('./travis/user_retweet_PREDICT8.txt', 'r').read())
m20 = eval(open('./travis/user_retweet_PREDICT9.txt', 'r').read())
m21 = eval(open('./travis/user_retweet_PREDICT7.txt', 'r').read())

n1 = eval(open('./yanxiao/userTopicCount_PREDICT1.txt', 'r').read())
n2 = eval(open('./yanxiao/userTopicCount_PREDICT2.txt', 'r').read())
n3 = eval(open('./yanxiao/userTopicCount_PREDICT3.txt', 'r').read())
n4 = eval(open('./yanxiao/userTopicCount_PREDICT4.txt', 'r').read())
n5 = eval(open('./yanxiao/userTopicCount_PREDICT5.txt', 'r').read())
n6 = eval(open('./yanxiao/userTopicCount_PREDICT6.txt', 'r').read())
n7 = eval(open('./yanxiao/userTopicCount_PREDICT7.txt', 'r').read())
n8 = eval(open('./yanxiao/userTopicCount_PREDICT8.txt', 'r').read())
n9 = eval(open('./yanxiao/userTopicCount_PREDICT9.txt', 'r').read())
n10 = eval(open('./yanxiao/userTopicCount_PREDICT10.txt', 'r').read())
n11 = eval(open('./yanxiao/userTopicCount_PREDICT11.txt', 'r').read())
n12 = eval(open('./yanxiao/userTopicCount_PREDICT12.txt', 'r').read())
n13 = eval(open('./travis/userTopicCount_PREDICT1.txt', 'r').read())
n14 = eval(open('./travis/userTopicCount_PREDICT2.txt', 'r').read())
n15 = eval(open('./travis/userTopicCount_PREDICT3.txt', 'r').read())
n16 = eval(open('./travis/userTopicCount_PREDICT4.txt', 'r').read())
n18 = eval(open('./travis/userTopicCount_PREDICT5.txt', 'r').read())
n19 = eval(open('./travis/userTopicCount_PREDICT6.txt', 'r').read())
n17 = eval(open('./travis/userTopicCount_PREDICT7.txt', 'r').read())
n20 = eval(open('./travis/userTopicCount_PREDICT8.txt', 'r').read())
n21 = eval(open('./travis/userTopicCount_PREDICT9.txt', 'r').read())

retweet_dict_TEST = {**f1, **f2, **f3, **f4, **f5, **f6, **f7, **f8,
                     **f9, **f10, **f11, **f12, **f13, **f14, **f15,
                     **f16, **f17, **f18, **f19, **f20, **f21, **f22,
                     **f23, **f24, **f25}

topic_number_dict_TEST = {**g1, **g2, **g3, **g4, **g5, **g6, **g7, **g8,
                     **g9, **g10, **g11, **g12, **g13, **g14, **g15,
                     **g16, **g17, **g18, **g19, **g20, **g21, **g22,
                     **g23, **g24, **g25}

retweet_dict_PREDICT = {**m1, **m2, **m3, **m4, **m5, **m6, **m7, **m8,
                     **m9, **m10, **m11, **m12, **m13, **m14, **m15,
                        **m16, **m17, **m18, **m19, **m20, **m21}

topic_number_dict_PREDICT = {**n1, **n2, **n3, **n4, **n5, **n6, **n7, **n8,
                     **n9, **n10, **n11, **n12, **n13, **n14, **n15,
                     **n16, **n17, **n18, **n19, **n20, **n21}

output_retweet_dict_TEST = open('retweet_dict_TEST.txt', 'w')
output_retweet_dict_PREDICT = open('retweet_dict_PREDICT.txt', 'w')
output_topic_number_dict_TEST = open('topic_number_dict_TEST.txt', 'w')
output_topic_number_dict_PREDICT = open('topic_number_dict_PREDICT.txt', 'w')

output_retweet_dict_TEST.write(str(retweet_dict_TEST))
output_retweet_dict_PREDICT.write(str(retweet_dict_PREDICT))
output_topic_number_dict_TEST.write(str(topic_number_dict_TEST))
output_topic_number_dict_PREDICT.write(str(topic_number_dict_PREDICT))

output_retweet_dict_TEST.close()
output_retweet_dict_PREDICT.close()
output_topic_number_dict_PREDICT.close()
output_topic_number_dict_TEST.close()
                     

 
