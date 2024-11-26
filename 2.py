import re  

with open('task2.html', encoding='utf-8') as file:  
    text = file.read()  
res3 = re.findall(r"(?<=font-family:\s').+(?=';)", text) 
print(res3)