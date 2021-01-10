import json
import re
with open(r"D:\Graduation Courses\Semester 2\NLP\Project\project_git\CSE-576-NR-2\stage1_test.json",'r+') as f:
    data1 = f.read()
with open(r"D:\Graduation Courses\Semester 2\NLP\Project\project_git\CSE-576-NR-2\stage2_test.json",'r+') as f:
    data2 = f.read()  
with open(r"D:\Graduation Courses\Semester 2\NLP\Project\project_git\CSE-576-NR-2\stage3_test.json",'r+') as f:
    data3 = f.read()  
    
data = data1 + data2 + data3 

start = 0
dataset = {}
count = 1
passageid_queryid = {}

for i in range(len(data)):
    if data[i]=='}':
        qap,d,r = {},{},{}
        res = data[start:i+1]
        d = json.loads(res)
        q = d["Question"]
        x = d["Id"]
        sr = q.split('.')
        r["passage"] = ""
        for j in range(len(sr)-1):
            if j==0: r["passage"] += sr[j]
            else: r["passage"] += ". "+sr[j]
        qap["question"] = sr[-1]
        qap["query_id"] = x
        r["qa_pairs"] = [qap]
        passageid = "passage_"+str(count)
        passageid_queryid[x] = passageid
        dataset[passageid] = r
        count += 1
        start = i+2

with open('allstage_test_processed_data.json','w',encoding = 'utf-8') as f:
    json.dump(dataset,f,ensure_ascii=False,indent=4)
    

with open(r"D:\Graduation Courses\Semester 2\NLP\Project\project_git\CSE-576-NR-2\stage1_test_with_answer.json",'r+') as f:
    data1 = f.read()
with open(r"D:\Graduation Courses\Semester 2\NLP\Project\project_git\CSE-576-NR-2\stage2_test_with_answer.json",'r+') as f:
    data2 = f.read()  
with open(r"D:\Graduation Courses\Semester 2\NLP\Project\project_git\CSE-576-NR-2\stage3_test_with_answer.json",'r+') as f:
    data3 = f.read()  
    
start = 0
dataset = {}
data = data1 + data2 + data3 

for i in range(len(data)):
    if data[i]=='}':
        qap,d,r,ans,dat = {},{},{},{},{}
        dat["day"] = ""
        dat["month"]  = ""
        dat["year"] = ""
        res = data[start:i+1]
        d = json.loads(res)
        q = d["Question"]
        a = d["Answer"]
        x = d["Id"]
        sr = q.split('.')
        r["passage"] = ""
        for j in range(len(sr)-1):
            if j==0: r["passage"] += sr[j]
            else: r["passage"] += ". "+sr[j]
        qap["question"] = sr[-1]
        ans["number"] = ""
        ans["date"] = dat
        ans["spans"] = []
        if re.search('[a-zA-Z]',a):
            ans["spans"].append(a)
        else: 
            ans["number"] = a
        qap["answer"] = ans
        qap["query_id"] = x
        r["qa_pairs"] = [qap]
        passageid = passageid_queryid[x]
        dataset[passageid] = r
        start = i+2

with open('allstage_test_processed_with_answer_data.json','w',encoding = 'utf-8') as f:
    json.dump(dataset,f,ensure_ascii=False,indent=4)