# app.py
students = ["Aliyev Vali", "Karimova Nodira", "Rahimov Sardor"]
groups = {"303": ["Aliyev Vali", "Karimova Nodira"], "304": ["Rahimov Sardor"]}

def list_students():
    for i, s in enumerate(students, 1):
        print(f"{i}. {s}")

def add_student(name):
    students.append(name)
    print(f"Qo'shildi: {name}")

if __name__ == "__main__":
    list_students()
    add_student("Soliyev Jasur")
