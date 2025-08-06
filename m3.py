def frequency_of_word(string):
    out_dict={}
    for word in string:
        if out_dict.get(word,0)==0:
            out_dict[word]=1
        else:
            out_dict[word]+=1
    return out_dict
print(frequency_of_word(input().split()))        
