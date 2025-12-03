students = []
for i in range(3):
    name = input("نام؟:")
    avg = float(input("معدل؟:"))
    courses = set()
    for j in range(2):
        course = input("دروس انتخابی؟:")
        courses.add(course)
    student ={"name":name,"moadel":avg,"corses":courses}
    students.append(student)
for s in students :
    print(s)