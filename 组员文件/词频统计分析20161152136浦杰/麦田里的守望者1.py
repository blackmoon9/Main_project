import jieba
txt = open("mtldswz.txt", encoding="utf-8").read()
words  = jieba.lcut(txt)
#定义空集合，并借此进行进行统计：

counts = {}  
for word in words:  
    counts[word] = counts.get(word,0) + 1
#dict_items转换为列表,并以第二个元素排序：
items = list(counts.items())  
items.sort(key=lambda x:x[1], reverse=True)
#以格式化打印前30名：
for i in range(30):  
    word, count = items[i]  
    print ("{0:<10}{1:>5}".format(word, count))
       

