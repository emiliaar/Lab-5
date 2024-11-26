import re
import csv

with open('task3.txt', encoding='utf-8') as file:  
    text = file.read() 

sites = re.findall(r'https?://[a-zA-Z0-9.-]+/', text)
text = re.sub(r'https?://[a-zA-Z0-9.-]+/', ' ', text)

dates = re.findall(r'\d{4}-\d{2}-\d{2}', text)
text = re.sub(r'\d{4}-\d{2}-\d{2}', ' ', text)

surnames = re.findall(r'[A-Z][a-z]+(?!\d\d@|@)', text)
text = re.sub(r'[A-Z][a-z]+(?!\d\d@|@)', ' ', text)

email_endings = set(re.findall(r'(?<=\.)[a-z]+(?=\s)', text))#'net', 'com', 'biz', 'info', 'org'
emails = re.findall(r'[a-z][a-z0-9-]*@[a-z0-9-]+\.[netcombizinfoorg]{3}o?', text)
text = re.sub(r'[a-z][a-z0-9-]*@[a-z0-9-]+\.[netcombizinfoorg]{3}o?', ' ', text)

id = 1
ids = []
while str(id) in text:
    ids += [id]
    id +=1

data = [['ID', 'Surname', 'Date', 'Email', 'Site']]
data += [list(_) for _ in list(zip(ids, surnames, dates, emails, sites))]
with open('3.csv', mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(data)