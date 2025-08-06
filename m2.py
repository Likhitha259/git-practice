# print('this is file2 for practise')
# '''this change is made in the github to know how the changes happen'''
a=[1,2,9.8,{'a':7},'iu',[2,3,4]]
b='a'
for i in a:
    if type(i)==dict:
        if b in i.keys():
           i[b]=34
print(a)