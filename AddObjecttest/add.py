
positionSeq_data=[[1,2],[2,3]]
print(len(positionSeq_data))
i=0
#確認用
###########################################################
print(f"positionSeq_data型:{type(positionSeq_data)}")
###########################################################
for datas in positionSeq_data:
       print("data1",data)
       for data in datas:
            
            if(i%2==0):
                print("x",data)
                i+=1
            else:
                print("y",data)
                i+=1
new=[0,0]
positionSeq_data.append(new)
#確認用
###########################################################
print(f"あああああああああああああああああああああああああああああああああああああpositionSeq_data型:{type(positionSeq_data)}")
###########################################################
i=0
for datas in positionSeq_data:
       print("data1")
       for data in datas:
            
            if(i%2==0):
                print("x",data)
                i+=1
            else:
                print("y",data)
                i+=1

