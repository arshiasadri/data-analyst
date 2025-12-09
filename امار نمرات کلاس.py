import numpy as np

# تولید نمرات تصادفی
grades = np.random.randint(0,21, size=100)

# محاسبات آماری
print("Average grades:",np.mean(grades))
print("min grade:",np.min(grades))
print("max grades:",np.max(grades))
print("Standard deviation:",np.std(grades))

# درصد قبولی
passed = grades[grades >= 10]
print("number of passed", len(passed),"from", len(grades))
print("percent of passed:",len(passed) / len(grades) * 100, "%")

# نمرات عالی
excellent = grades[grades > 17]
print("excellent grades:",excellent)

# مرتب سازی نمرات
print("sorted grades \n", np.sort(grades))