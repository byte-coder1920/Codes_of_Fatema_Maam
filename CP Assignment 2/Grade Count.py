#grade count
for i in range (0,5):
    marks = float(input("Obtained marks: "))
    if marks >=90:
        print("A+")
    elif marks >=80 and marks <90:
        print("A")
    elif marks>=70 and marks <80:
        print("B")
    elif marks>= 60 and marks < 70:
        print("c")
    elif marks >= 50 and marks < 60:
        print("D")
    elif marks >= 40 and marks < 50:
        print("E")
    else:
        print("Fail")



