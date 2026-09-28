obtained_marks=int(input("Enter obtained marks :"))
total_marks=int(input("Enter total marks :"))
percent=(obtained_marks/total_marks)*100
if percent >=90:
    print("A Grade")
elif percent >=80 :
    print("B Grade")
elif percent >=70:
    print("C Grade")
elif percent >=60 :
    print("D Grade")
elif percent >=50 :
    print("E Grade")