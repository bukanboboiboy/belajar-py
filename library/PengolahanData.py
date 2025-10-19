"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'London', 'Paris', 'Tokyo'],
    'Job': ['Engineer', 'Doctor', 'Artist', 'Chef']
}

df = pd.DataFrame(data)

print(df)

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(matrix)

x = [25, 30, 35, 40]
y = ['Engineer', 'Doctor', 'Artist', 'Chef']

# plt.plot(x, y)
# plt.title("Sample Plot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.show()

tips = sns.load_dataset("tips")
sns.histplot(tips['tip'], kde=True)
plt.show()
"""

import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import math

# import seaborn as sns

data_nilai = {
    "Nama": ["Andi", "Budi", "Citra", "Dodi", "Eka"],
    "Matematika": np.array([80, 90, 75, 85, 95]),
    "Fisika": np.array([70, 85, 80, 90, 100]),
    "Biologi": np.array([90, 80, 85, 75, 95]),
    "Kimia": np.array([75, 80, 90, 85, 100]),
    "Bahasa": np.array([85, 90, 80, 95, 100])
}

df_nilai = pd.DataFrame(data_nilai)
# print("Data Nilai Siswa:")
# print(df_nilai)


df_nilai["rata-rata"] = df_nilai[["Matematika",
                                  "Fisika", "Biologi",
                                  "Kimia", "Bahasa"]].mean(axis=1)

# print("\nRata-rata Nilai Siswa:")
# print(df_nilai[["Nama", "rata-rata"]])

"""
plt.figure(figsize=(10, 6))
plt.bar(df_nilai["Nama"], df_nilai["rata-rata"], color='skyblue')

plt.title("Rata-rata Nilai Siswa")
plt.xlabel("Nama Siswa")
plt.ylabel("Rata-rata Nilai")
plt.ylim(0, 100)
plt.show()
"""
max_rata = np.max(df_nilai[["rata-rata"]])

# Find the student with the highest average score
max_student = df_nilai.loc[df_nilai['rata-rata'] == max_rata, 'Nama'].values[0]
print(f"Student with highest average score: {max_student}")
