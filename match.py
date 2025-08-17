# it is similer to switch statment 

mounth =5
day =4
match (day):
    case  1 | 2 | 3| 4  if mounth ==5:
        print("sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("wednesdy")
    case 5:
        print("thresday")
    case _:
        print("nothing")
        