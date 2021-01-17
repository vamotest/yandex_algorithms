
def make_top_university(students, value):
    student_dict = {
        students_count:
            students.count(students_count)
        for students_count in set(students)
    }
    
    sorted_dict = {
        key: student_dict.get(key)
        for key in sorted(student_dict, key=student_dict.get, reverse=True)
    }
    top = list(sorted_dict.keys())[:value]
    return top
    
    
if __name__ == '__main__':
    students_list = list(map(int, input().split()))
    k = int(input())
    result = make_top_university(students_list, k)
    print(*result)
