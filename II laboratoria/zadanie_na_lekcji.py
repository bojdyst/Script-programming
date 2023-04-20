import sys

def add_course(course_list, course, max_number_of_courses):
    if course in course_list:
        return "This course already exists! Enter other name.\n"
    elif len(course_list) + 1 > max_number_of_courses:
        return "You reached the limit of available courses! Delete one to be able to create new one.\n"
    elif course not in course_list:
        course_list[course] = []
        return course_list
       
def add_to_course(course_list, course, person, max_number_of_attendants_in_group):
    if course not in course_list:
        return "There's no such a course! Enter valid one.\n"
    elif person in course_list[course]:
        return "This person is already regisered! Enter other name.\n"
    elif len(course_list[course]) + 1 > max_number_of_attendants_in_group:  
        return "You reached the limit of available places in this course! Enroll to other course or free space in this course.\n"
    elif person not in course_list[course]:
        course_list[course].append(person)
        return course_list     

def delete_from_course(course_list, course, person):
    if course not in course_list:
        return "There's no such a course! Enter valid one.\n"
    elif person not in course_list[course]:
        return "This person doesn't attend this course! Enter valid one.\n"
    elif person in course_list[course]:
        course_list[course].remove(person)
        return course_list

def modify_course(course_list, old_course_name, new_course_name):
    if (old_course_name in course_list) and (new_course_name not in course_list):
        course_list[new_course_name] = course_list.pop(old_course_name)
        return course_list
    elif old_course_name not in course_list:
        return "There's no such a course! Enter valid one.\n"
    elif new_course_name in course_list:
        return "This course already exists! Enter new one.\n"
    
def delete_course(course_list, course):
    if course not in course_list:
        return "There's no such a course! Enter valid one.\n"
    elif course in course_list:
        del course_list[course]
        return course_list

if __name__ == "__main__":
    max_number_of_courses = int(sys.argv[1])
    max_number_of_attendants_in_group = int(sys.argv[2])

    course_list = {}

    while True:
        try:
            user_input = input("What are You gonna do? Type proper number and required informations:\n\
                add_course => 1 + course_name\n\
                modify_course => 2 + old_name + new_name\n\
                delete_course => 3 + course_name\n\
                add_to_course => 4 + course_name + attendant_name\n\
                delete_from_course => 5 + course_name + attendant_name\n").split(" ")

            match user_input[0]:
                case "1":
                    print(add_course(course_list, user_input[1], max_number_of_courses))
                case "2":
                    print(modify_course(course_list, user_input[1], user_input[2]))
                case "3":
                    print(delete_course(course_list, user_input[1]))
                case "4":
                    print(add_to_course(course_list, user_input[1], user_input[2], max_number_of_attendants_in_group))
                case "5":
                    print(delete_from_course(course_list, user_input[1], user_input[2]))
        except KeyboardInterrupt:
            print(course_list)
            exit()