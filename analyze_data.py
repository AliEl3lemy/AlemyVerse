import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Read the data file
df = pd.read_csv('tech_salaries.csv')

# ==========================================
# Chart 1: Average Salary by Job Title (Bar Chart)
# ==========================================
avg_salary_by_job = df.groupby('Job_Title')['Salary_USD'].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x=avg_salary_by_job.values, y=avg_salary_by_job.index, palette='viridis')

plt.title('Average Annual Salary by Job Title')
plt.xlabel('Average Salary (USD)')
plt.ylabel('Job Title')
plt.tight_layout()

# Save the first chart as an image
plt.savefig('salary_by_job.png', dpi=300)
print("✅ First chart saved successfully: 'salary_by_job.png'")
plt.close() # Close the figure to start a new one cleanly

# ==========================================
# Chart 2: Work Type Distribution (Pie Chart)
# ==========================================
work_type_counts = df['Work_Type'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(work_type_counts, labels=work_type_counts.index, autopct='%1.1f%%', 
        colors=['#ff9999','#66b3ff','#99ff99'], startangle=90)

plt.title('Work Type Distribution (Remote vs On-site vs Hybrid)')
plt.tight_layout()

# Save the second chart as an image
plt.savefig('work_type_distribution.png', dpi=300)
print("✅ Second chart saved successfully: 'work_type_distribution.png'")
plt.close()

print("🚀 Data analysis complete! All charts are ready for your portfolio.")