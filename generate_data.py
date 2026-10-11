import pandas as pd
import random
import numpy as np
print("Loading Data Upload...")
job_titles = ['Software Engineer', 'Data Scientist', 'Data Analysist', 'Machine Learing Engineer', 
'DevOps Engineer', 'Web Developer']
experience_levels = ['junior', 'Mid-Level', 'Senior', 'Expert']
work_types = ['Remote', 'on-site', 'Hybrid']
company_sizes = ['small', 'Medium', 'Large']
data = []
for _ in range(1000):
    job = random.choice(job_titles)
    exp = random.choice(experience_levels)
    work = random.choice(work_types)
    size = random.choice(company_sizes)
    base_salary = 5000
    if exp == 'Mid-Level': base_salary+= 30000
    elif exp == 'Senior': base_salary+= 70000
    elif exp == 'Expert': base_salary+= 110000
    if job in ['Data Scientist', 'Machine Learing Engineer']:base_salary += 20000 
    if size == 'Large': base_salary += 15000

    salary = int(np.random.normal(base_salary,base_salary * 0.1))
    data.append([job, exp, work, size, salary])
df = pd.DataFrame(data,columns=['Job_Title', 'Experience_Level', 'Work_Type', 'company_Size', 'Salary_USD'])
df.to_csv('tech_salaries.csv',index=False)
print("Data file 'tech_salaries.csv' created successfully! Ready for analysis")