def cal_total_marks(marks):
    total=sum(marks)
    return total

def cal_average_marks(total,n):
    avg=total/n
    return avg

def cal_grade(average_marks):
    if average_marks>90:
        grade='S'
    elif average_marks<90 and average_marks>85:
        grade='A+'
    elif average_marks<85 and average_marks>75:
        grade='A'
    elif average_marks<75 and average_marks>65:
        grade='B'
    elif average_marks<65 and average_marks>55:
        grade='C'
    elif average_marks<55 and average_marks>50:
        grade='D'
    else:
        grade='F'

    return grade

def student(marks):
    total_marks=cal_total_marks(marks)
    num_sub=len(marks)
    average_marks=cal_average_marks(total_marks,num_sub)
    grade=cal_grade(average_marks)
    stu=[average_marks,grade]
    return stu
    
