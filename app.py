# app.py
students = ["Aliyev Vali", "Karimova Nodira", "Rahimov Sardor"]

def list_students():
    for i, s in enumerate(students, 1):
        print(f"{i}. {s}")

if __name__ == "__main__":
    list_students()
