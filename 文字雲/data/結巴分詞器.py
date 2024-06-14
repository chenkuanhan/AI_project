import jieba


data={}

text_file = open(r'C:\Users\hank\Desktop\run\data\19Congress.txt','r',encoding='utf-8')
text = text_file.read()
with open(r'C:\Users\hank\Desktop\run\data\19Congress.txt',encoding='utf-8') as file:
    stopwords = {line.strip() for line in file}

seg_list = jieba.cut(text, cut_all=False)
for word in seg_list:
    if len(word)>=2:
        if not data.__contains__(word):
            data[word]=0
        data[word]+=1
print(data)