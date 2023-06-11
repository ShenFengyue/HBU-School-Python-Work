import pandas as pd

# Read the Excel file
df = pd.read_excel('D:\\桌面\\Python\\每周Python作业\\第十三周\\data1.xlsx')

# Grouping and counting based on a specific column
grouped_data = df.groupby('gender').size().reset_index(name='Count')

# Display the grouped and counted data
print(grouped_data)


