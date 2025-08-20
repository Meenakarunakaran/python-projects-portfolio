students=[]
def add_student(name, age, course):
    student={"name": name, "age": age, "course": course}
    students.append(student)
def display_students():
    for s in students:
        print(f"Name: {s['name']}, Age: {s['age']}, Course: {s['course']}")
add_student("Queena", 20, "Computer Science")
add_student("Alice", 22, "Mathematics")
display_students()         

