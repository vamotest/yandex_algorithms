
def main():
    visited_optional_courses = set()
    
    for _ in range(int(input())):
        course = input()
        
        if course not in visited_optional_courses:
            visited_optional_courses.add(course)
            print(course)


if __name__ == '__main__':
    main()