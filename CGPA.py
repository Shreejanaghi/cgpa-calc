import pandas as pd
import json

filenames=["C:/Users/shree/Documents/input1.csv","C:/Users/shree/Documents/input2.csv"] 

gpa_dict={}

sum_semesters=0
sum_gpa=0.0
credits_gained=0

for filename in filenames:
    data=pd.read_csv(filename)
    grade_points={'O': 10, 'A+': 9, 'A': 8, 'B+': 7, 'B': 6, 'C': 5, 'RA': 0}
    sum_points=0
    sum_credits=0
    for index in range(len(data)):
        grade=data.loc[index,'grade']
        credits=data.loc[index,'credits']
        if grade!='RA':
            sum_points+=grade_points.get(grade, 0) * credits
            sum_credits+=credits
        
    semester_gpa=sum_points/sum_credits

    gpa_dict[filename] = {'GPA':float(semester_gpa), 'Credits Gained':int(sum_credits)}

    sum_semesters+=1
    sum_gpa+=semester_gpa
    credits_gained+=sum_credits

cgpa=sum_gpa/sum_semesters

output_data={'Semester GPAs':gpa_dict,'CGPA':float(cgpa),'Credits_gained':int(credits_gained)}
json_output=json.dumps(output_data,indent=0)
print(json_output)
