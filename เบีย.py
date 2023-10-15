import pandas as pd
from scipy.stats import ttest_ind

# ตัวอย่างการโหลดข้อมูลจาก CSV file
# แน่นอน, คุณต้องแทนที่ 'your_file.csv' ด้วยเส้นทางที่ถูกต้องของไฟล์ข้อมูลของคุณ

# file_path = "your_file.csv"
# df_new2 = pd.read_csv(file_path)

# ตัวอย่างนี้ใช้ข้อมูลที่สร้างขึ้นเป็นตัวอย่าง
data = {
    'Age_Group': ['Middle-age', 'Old-age', 'Middle-age', 'Old-age'],
    'Attribute1': [10, 20, 30, 40],
    'Attribute2': [5, 15, 25, 35],
    'Attribute3': [1, 2, 3, 4]
}

df_new2 = pd.DataFrame(data)

# ทำการแบ่งกลุ่มข้อมูล
group1 = df_new2[df_new2['Age_Group']=='Middle-age']
group2 = df_new2[df_new2['Age_Group']=='Old-age']

# สร้าง DataFrame ว่างสำหรับเก็บผลลัพธ์
results_df = pd.DataFrame(columns=['Attribute', 'pvalue'])

# ทดสอบสถิติสำหรับทุกคอลัมน์และเก็บผลลัพธ์
for columnName in df_new2.columns[1:]:  # ข้ามคอลัมน์ 'Age_Group'
    print(f"Processing {columnName}...")
    try:
        t, pvalue = ttest_ind(group1[columnName], group2[columnName])
        results_df = results_df.append({'Attribute': columnName, 'pvalue': pvalue}, ignore_index=True)
    except Exception as e:
        print(f"Cannot process {columnName}: {str(e)}")
        continue

# เรียงลำดับผลลัพธ์ตาม p-value และแสดงผล
results_df = results_df.sort_values(by='pvalue')
print(results_df)

