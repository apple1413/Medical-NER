#encoding=utf8
import csv,os,jieba
import jieba.posseg as pseg
rowCount=0
dev=open("./data/example.dev",'w',encoding='utf8')
train=open("./data/example.train",'w',encoding='utf8')
test=open("./data/example.test",'w',encoding='utf8')
biaoji = set(['DIS', 'SYM', 'SGN', 'TES', 'DRU', 'SUR', 'PRE', 'PT', 'DUR', 'TP', 'REG', 'ORG', 'AT', 'PSB', 'DEG', 'FW','CL'])
fuhao=['!','。','！','?','？']
dics=csv.reader(open(r"E:\NERuselocal4\NERuselocal\data\example.train",'r',encoding='utf-8'))
for row in dics:
    if len(row)==2:
        jieba.add_word(row[0].strip(), tag=row[1].strip())
        jieba.suggest_freq(row[0].strip)
split_num=0
for file in os.listdir('./source'):
    if 'txtoriginal' in  file:
        fp=open('./spurce/'+file,'r',encoding='utf-8')
        for line in fp:
            split_num+=1
            words=pseg.cut(line)
            for key,value in words:
                if value.strip() and key.strip():
                     import  time
                     start_time=time.time()
                     index=str(1) if split_num%1515<2 else str(2) if split_num %15<4 else str(3)
                     end_time=time.time()
                     print('method can useed time is {}'.format(end_time-start_time))
                     if value not in biaoji:
                        value='O'
                        for achar in key.strip():
                            if achar and achar.strip() in fuhao:
                                string=achar+" "+value.strip()+'\n'+'\n'
                            elif achar.strip() and achar.strip() not in fuhao:
                                string = achar + " " + value.strip() + '\n'
                                dev.write(string) if index=='1' else test.write(string) if index=='2' else train.write(string)
                     elif value.strip() in biaoji:
                          begin=0
                          for char in key.strip():
                              if begin==0:
                                  begin+=1
                                  string=char+' '+'B-'+value.strip()+'\n'
                                  if index=='1':
                                      dev.write(string)
                                  elif index=='2':
                                      test.write(string)
                                  elif index=='3':
                                      train.write(string)
                                  else:
                                      pass
                              else:
                                  string = char + ' ' + 'I-' + value.strip() + '\n'
                                  if index == '1':
                                      dev.write(string)
                                  elif index == '2':
                                      test.write(string)
                                  elif index == '3':
                                      train.write(string)
                                  else:
                                      pass

#
# for row in rows:
#     if flag==0:
#         flag=1
#         continue
#     if len(row)==6 and devFlag :
#         rowCount+=1
#         if rowCount<lenthTotal/15-1:
#             if row[2].strip() and row[2].strip() not in huanhang:
#                 for a in row[2].strip():
#                     if row[3].strip()=='O':
#                         dev.write(a.strip()+" "+row[3].strip()+"\n")
#                     else:
#                         if a==row[2].strip()[0]:
#                             string = a.strip() + " " + "B-" + row[3].strip()
#                             text = string.split( )
#                             assert len(text) == 2
#                             dev.write(a.strip() + " " + "B-"+ row[3].strip()+ "\n")
#                         else:
#                             string = a.strip() + " " + "I-" + row[3].strip()
#                             text = string.split( )
#                             assert len(text) == 2
#                             dev.write(a.strip() + " " + "I-" + row[3].strip() + "\n")
#             else:
#                 string = row[2].strip() + " " + row[3].strip()
#                 text = string.split( )
#                 assert len(text) == 2
#                 if row[2].strip() and row[3].strip():
#                     dev.write(row[2].strip() + " " + row[3].strip() + "\n" + "\n")
#         else:
#             if row[2].strip() and row[2].strip() not in huanhang:
#                 for a in row[2].strip():
#                     if row[3].strip()=='O':
#                         dev.write(a.strip()+" "+row[3].strip()+"\n")
#                     else:
#                         if a==row[2].strip()[0]:
#                             string = a.strip() + " " + "B-" + row[3].strip()
#                             text = string.split( )
#                             assert len(text) == 2
#                             dev.write(a.strip() + " " + "B-"+row[3].strip()+ "\n")
#                         else:
#                             string = a.strip() + " " + "I-" + row[3].strip()
#                             text = string.split( )
#                             assert len(text) == 2
#                             dev.write(a.strip() + " " + "I-" + row[3].strip() + "\n")
#             else:
#                 string = row[2].strip() + " " + row[3].strip()
#                 text = string.split( )
#                 assert len(text) == 2
#                 devFlag=False
#                 testFlag=True
#                 if row[2].strip() and row[3].strip():
#                     dev.write(row[2].strip() + " " + row[3].strip() + "\n"+"\n")
#     if len(row)==6 and testFlag :
#         rowCount+=1
#         if rowCount > lenthTotal / 15 and rowCount < 2 * lenthTotal / 15-1 :
#             if row[2].strip() and row[2].strip() not in huanhang:
#                 for a in row[2].strip():
#                     if row[3].strip()=='O':
#                         test.write(a.strip()+" "+row[3].strip()+"\n")
#                     else:
#                         if a==row[2].strip()[0]:
#                             string = a.strip() + " " + "B-" + row[3].strip()
#                             text = string.split( )
#                             assert len(text) == 2
#                             test.write(a.strip() + " " + "B-"+ row[3].strip()+ "\n")
#                         else:
#                             string = a.strip() + " " + "I-" + row[3].strip()
#                             text = string.split( )
#                             assert len(text) == 2
#                             test.write(a.strip() + " " + "I-" + row[3].strip() + "\n")
#             else:
#                 string = row[2].strip() + " " + row[3].strip()
#                 text = string.split( )
#                 assert len(text) == 2
#                 if row[2].strip() and row[3].strip():
#                     test.write(row[2].strip() + " " + row[3].strip() + "\n" + "\n")
#         if rowCount >= 2 * lenthTotal / 15-1 and testFlag:
#             if row[2].strip() and row[2].strip() not in huanhang:
#                 for a in row[2].strip():
#                     if row[3].strip()=='O':
#                         test.write(a.strip()+" "+row[3].strip()+"\n")
#                     else:
#                         if a==row[2].strip()[0]:
#                             string = a.strip() + " " + "B-" + row[3].strip()
#                             text = string.split( )
#                             assert len(text) == 2
#                             test.write(a.strip() + " " + "B-"+row[3].strip()+ "\n")
#                         else:
#                             string = a.strip() + " " + "I-" + row[3].strip()
#                             text = string.split( )
#                             assert len(text) == 2
#                             test.write(a.strip() + " " + "I-" + row[3].strip() + "\n")
#             else:
#                 string = row[2].strip() + " " + row[3].strip()
#                 text = string.split( )
#                 assert len(text) == 2
#                 testFlag = False
#                 trainFlag=True
#                 if row[2].strip() and row[3].strip():
#                     test.write(row[2].strip() + " " + row[3].strip() + "\n" + "\n")
#     if len(row)==6 and trainFlag:
#         if row[2].strip() and row[2].strip() not in huanhang:
#             for a in row[2].strip():
#                 if row[3].strip() == 'O':
#                     train.write(a.strip() + " " + row[3].strip() + "\n")
#                 else:
#                     if a == row[2].strip()[0]:
#                         string = a.strip() + " " + "B-" + row[3].strip()
#                         text = string.split()
#                         assert len(text) == 2
#                         train.write(a.strip() + " " + "B-" + row[3].strip() + "\n")
#                     else:
#                         string = a.strip() + " " + "I-" + row[3].strip()
#                         text = string.split()
#                         assert len(text) == 2
#                         train.write(a.strip() + " " + "I-" + row[3].strip() + "\n")
#         else:
#             string = row[2].strip() + " " + row[3].strip()
#             text = string.split()
#             if len(text) != 2:
#                 print(string)
#             if row[2].strip() and row[3].strip():
#                 train.write(row[2].strip() + " " + row[3].strip() + "\n" + "\n")
#
# flag=0
# devFlag = True
# trainFlag = False
# testFlag = False
# rowCount=0
# for row in rows1:
#     if flag==0:
#         flag=1
#         continue
#     if len(row)==6 and devFlag :
#         rowCount+=1
#         if rowCount<lenthTotal/15-1:
#             if row[2].strip() and row[2].strip() not in huanhang:
#                 for a in row[2].strip():
#                     if row[3].strip()=='O':
#                         dev.write(a.strip()+" "+row[3].strip()+"\n")
#                     else:
#                         if a==row[2].strip()[0]:
#                             string = a.strip() + " " + "B-" + row[3].strip()
#                             text = string.split( )
#                             assert len(text) == 2
#                             dev.write(a.strip() + " " + "B-"+ row[3].strip()+ "\n")
#                         else:
#                             string = a.strip() + " " + "I-" + row[3].strip()
#                             text = string.split( )
#                             assert len(text) == 2
#                             dev.write(a.strip() + " " + "I-" + row[3].strip() + "\n")
#             else:
#                 string = row[2].strip() + " " + row[3].strip()
#                 text = string.split( )
#                 assert len(text) == 2
#                 if row[2].strip() and row[3].strip():
#                     dev.write(row[2].strip() + " " + row[3].strip() + "\n" + "\n")
#         else:
#             if row[2].strip() and row[2].strip() not in huanhang:
#                 for a in row[2].strip():
#                     if row[3].strip()=='O':
#                         dev.write(a.strip()+" "+row[3].strip()+"\n")
#                     else:
#                         if a==row[2].strip()[0]:
#                             string = a.strip() + " " + "B-" + row[3].strip()
#                             text = string.split( )
#                             assert len(text) == 2
#                             dev.write(a.strip() + " " + "B-"+row[3].strip()+ "\n")
#                         else:
#                             string = a.strip() + " " + "I-" + row[3].strip()
#                             text = string.split( )
#                             assert len(text) == 2
#                             dev.write(a.strip() + " " + "I-" + row[3].strip() + "\n")
#             else:
#                 string = row[2].strip() + " " + row[3].strip()
#                 text = string.split( )
#                 assert len(text) == 2
#                 devFlag=False
#                 testFlag=True
#                 if row[2].strip() and row[3].strip():
#                     dev.write(row[2].strip() + " " + row[3].strip() + "\n"+"\n")
#     if len(row)==6 and testFlag :
#         rowCount+=1
#         if rowCount > lenthTotal / 15 and rowCount < 2 * lenthTotal / 15-1 :
#             if row[2].strip() and row[2].strip() not in huanhang:
#                 for a in row[2].strip():
#                     if row[3].strip()=='O':
#                         test.write(a.strip()+" "+row[3].strip()+"\n")
#                     else:
#                         if a==row[2].strip()[0]:
#                             string = a.strip() + " " + "B-" + row[3].strip()
#                             text = string.split( )
#                             assert len(text) == 2
#                             test.write(a.strip() + " " + "B-"+ row[3].strip()+ "\n")
#                         else:
#                             string = a.strip() + " " + "I-" + row[3].strip()
#                             text = string.split( )
#                             assert len(text) == 2
#                             test.write(a.strip() + " " + "I-" + row[3].strip() + "\n")
#             else:
#                 string = row[2].strip() + " " + row[3].strip()
#                 text = string.split( )
#                 assert len(text) == 2
#                 if row[2].strip() and row[3].strip():
#                     test.write(row[2].strip() + " " + row[3].strip() + "\n" + "\n")
#         if rowCount >= 2 * lenthTotal / 15-1 and testFlag:
#             if row[2].strip() and row[2].strip() not in huanhang:
#                 for a in row[2].strip():
#                     if row[3].strip()=='O':
#                         test.write(a.strip()+" "+row[3].strip()+"\n")
#                     else:
#                         if a==row[2].strip()[0]:
#                             string = a.strip() + " " + "B-" + row[3].strip()
#                             text = string.split( )
#                             assert len(text) == 2
#                             test.write(a.strip() + " " + "B-"+row[3].strip()+ "\n")
#                         else:
#                             string = a.strip() + " " + "I-" + row[3].strip()
#                             text = string.split( )
#                             assert len(text) == 2
#                             test.write(a.strip() + " " + "I-" + row[3].strip() + "\n")
#             else:
#                 string = row[2].strip() + " " + row[3].strip()
#                 text = string.split( )
#                 assert len(text) == 2
#                 testFlag = False
#                 trainFlag=True
#                 if row[2].strip() and row[3].strip():
#                     test.write(row[2].strip() + " " + row[3].strip() + "\n" + "\n")
#     if len(row)==6 and trainFlag:
#         if row[2].strip() and row[2].strip() not in huanhang:
#             for a in row[2].strip():
#                 if row[3].strip() == 'O':
#                     train.write(a.strip() + " " + row[3].strip() + "\n")
#                 else:
#                     if a == row[2].strip()[0]:
#                         string = a.strip() + " " + "B-" + row[3].strip()
#                         text = string.split()
#                         assert len(text) == 2
#                         train.write(a.strip() + " " + "B-" + row[3].strip() + "\n")
#                     else:
#                         string = a.strip() + " " + "I-" + row[3].strip()
#                         text = string.split()
#                         assert len(text) == 2
#                         train.write(a.strip() + " " + "I-" + row[3].strip() + "\n")
#         else:
#             string = row[2].strip() + " " + row[3].strip()
#             text = string.split()
#             assert len(text) == 2
#             if row[2].strip() and row[3].strip():
#                 train.write(row[2].strip() + " " + row[3].strip() + "\n" + "\n")
#
#
# flag=0
# devFlag = True
# trainFlag = False
# testFlag = False
# rowCount=0
# for row in rows2:
#     if flag==0:
#         flag=1
#         continue
#     if len(row)==6 and devFlag :
#         rowCount+=1
#         if rowCount<lenthTotal/15-1:
#             if row[2].strip() and row[2].strip() not in huanhang:
#                 for a in row[2].strip():
#                     if row[3].strip()=='O':
#                         dev.write(a.strip()+" "+row[3].strip()+"\n")
#                     else:
#                         if a==row[2].strip()[0]:
#                             string = a.strip() + " " + "B-" + row[3].strip()
#                             text = string.split( )
#                             assert len(text) == 2
#                             dev.write(a.strip() + " " + "B-"+ row[3].strip()+ "\n")
#                         else:
#                             string = a.strip() + " " + "I-" + row[3].strip()
#                             text = string.split( )
#                             assert len(text) == 2
#
#                             dev.write(a.strip() + " " + "I-" + row[3].strip() + "\n")
#             else:
#                 string = row[2].strip() + " " + row[3].strip()
#                 text = string.split( )
#                 assert len(text) == 2
#                 if row[2].strip() and row[3].strip():
#                     dev.write(row[2].strip() + " " + row[3].strip() + "\n" + "\n")
#         else:
#             if row[2].strip() and row[2].strip() not in huanhang:
#                 for a in row[2].strip():
#                     if row[3].strip()=='O':
#                         dev.write(a.strip()+" "+row[3].strip()+"\n")
#                     else:
#                         if a==row[2].strip()[0]:
#                             string = a.strip() + " " + "B-" + row[3].strip()
#                             text = string.split( )
#                             assert len(text) == 2
#                             dev.write(a.strip() + " " + "B-"+row[3].strip()+ "\n")
#                         else:
#                             string = a.strip() + " " + "I-" + row[3].strip()
#                             text = string.split( )
#                             assert len(text) == 2
#                             dev.write(a.strip() + " " + "I-" + row[3].strip() + "\n")
#             else:
#                 devFlag=False
#                 testFlag=True
#                 string = row[2].strip() + " " + row[3].strip()
#                 text = string.split( )
#                 assert len(text) == 2
#                 if row[2].strip() and row[3].strip():
#                     dev.write(row[2].strip() + " " + row[3].strip() + "\n"+"\n")
#     if len(row)==6 and testFlag :
#         rowCount+=1
#         if rowCount > lenthTotal / 15 and rowCount < 2 * lenthTotal / 15-1 :
#             if row[2].strip() and row[2].strip() not in huanhang:
#                 for a in row[2].strip():
#                     if row[3].strip()=='O':
#                         test.write(a.strip()+" "+row[3].strip()+"\n")
#                     else:
#                         if a==row[2].strip()[0]:
#                             string = a.strip() + " " + "B-" + row[3].strip()
#                             text = string.split( )
#                             assert len(text) == 2
#                             test.write(a.strip() + " " + "B-"+ row[3].strip()+ "\n")
#                         else:
#                             string = a.strip() + " " + "I-" + row[3].strip()
#                             text = string.split( )
#                             assert len(text) == 2
#                             test.write(a.strip() + " " + "I-" + row[3].strip() + "\n")
#             else:
#                 string = row[2].strip() + " " + row[3].strip()
#                 text = string.split()
#                 assert len(text) == 2
#                 if row[2].strip() and row[3].strip():
#                     test.write(row[2].strip() + " " + row[3].strip() + "\n" + "\n")
#         if rowCount >= 2 * lenthTotal / 15-1 and testFlag:
#             if row[2].strip() and row[2].strip() not in huanhang:
#                 for a in row[2].strip():
#                     if row[3].strip()=='O':
#                         string = a.strip() + " " + row[3].strip()
#                         text = string.split( )
#                         assert len(text) == 2
#                         test.write(a.strip()+" "+row[3].strip()+"\n")
#                     else:
#                         if a==row[2].strip()[0]:
#                             string = a.strip() + " " + "B-" + row[3].strip()
#                             text = string.split( )
#                             assert len(text) == 2
#                             test.write(a.strip() + " " + "B-"+row[3].strip()+ "\n")
#                         else:
#                             string = a.strip() + " " + "I-" + row[3].strip()
#                             text = string.split( )
#                             assert len(text) == 2
#                             test.write(a.strip() + " " + "I-" + row[3].strip() + "\n")
#             else:
#
#                 testFlag = False
#                 trainFlag=True
#                 string = row[2].strip() + " " + row[3].strip()
#                 text = string.split( )
#                 assert len(text) == 2
#                 if row[2].strip() and row[3].strip():
#                     test.write(row[2].strip() + " " + row[3].strip() + "\n" + "\n")
#     if len(row)==6 and trainFlag:
#         if row[2].strip() and row[2].strip() not in huanhang:
#             for a in row[2].strip():
#                 if row[3].strip() == 'O':
#                     string = a.strip() + " " + row[3].strip()
#                     text = string.split( )
#                     assert len(text) == 2
#                     train.write(a.strip() + " " + row[3].strip() + "\n")
#                 else:
#                     if a == row[2].strip()[0]:
#                         string=a.strip() + " " + "B-" + row[3].strip()
#                         text=string.split( )
#                         assert  len(text)==2
#                         train.write(a.strip() + " " + "B-" + row[3].strip() + "\n")
#                     else:
#                         string=a.strip() + " " + "I-" + row[3].strip()
#                         text=string.split( )
#                         assert  len(text)==2
#                         train.write(a.strip() + " " + "I-" + row[3].strip() + "\n")
#         else:
#             string = row[2].strip() + " " + row[3].strip()
#             text = string.split( )
#             assert len(text) == 2
#             if row[2].strip() and row[3].strip():
#                 train.write(row[2].strip() + " " + row[3].strip() + "\n" + "\n")

dev.close()
test.close()
train.close()
