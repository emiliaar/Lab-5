import re  
 
with open('task1-en.txt', encoding='utf-8') as file:  
    text = file.read()  
res1 = re.findall(r'\b[Cc][a-zA-Z]+', text)  
res2 = re.findall(r'(?<=\b[Tt]he\s)[a-zA-Z]{2,}', text) 
print(res1) 
print(res2) 