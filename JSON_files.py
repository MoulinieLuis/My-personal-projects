import json

data = {"name": "Luis", "age": 21, "city": "Mexico City", "skills": ["Python", "C", "SQL", "SysAdmin"], "is_student": True, "Employer": "Huawei Mexico"}

with open("data.json", "w") as file:
    json.dump(data, file)
