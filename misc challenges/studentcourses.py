# You are a developer for a university. Your current project is to develop a system for students to find
# courses they share with friends. The university has a system for querying courses students are enrolled
# in, returned as a list of (ID, course) pairs.

# Write a function that takes in a list of (student ID number, course name) pairs and returns, for every
# pair of students, a list of all courses they share.

# Sample Input:
# student_course_pairs = [
#     ["58", "Software Design"],
#     ["58", "Linear Algebra"],
#     ["94", "Art History"],
#     ["94", "Operating Systems"],
#     ["17", "Software Design"],
#     ["58", "Mechanics"],
#     ["58", "Economics"],
#     ["17", "Linear Algebra"],
#     ["17", "Political Science"],
#     ["94", "Economics"]
# ]

# Sample Output (pseudocode, in any order)

# find_pairs(student_course_pairs) =>
# {
#     [58, 17]: ["Software Design", "Linear Algebra"]
#     [58, 94]: ["Economics"]
#     [17, 94]: []
# }


def find_pairs(student_course_pairs):
    students = []
    studentCourses, res = {}, {}

    for cur in student_course_pairs:
        if cur[0] not in studentCourses:
            studentCourses[cur[0]] = [cur[1]]
            students.append(cur[0])
        else:
            studentCourses[cur[0]].append(cur[1])

    # print(students)
    # print(studentCourses)
    for i in range(len(students) - 1):
        for j in range(i + 1, len(students)):
            first, second = students[i], students[j]
            seen = set(studentCourses[first])
            res[(first, second)] = []

            for cur in studentCourses[second]:
                if cur in seen:
                    res[(first, second)].append(cur)
    return res


student_course_pairs = [
    ["58", "Software Design"],
    ["58", "Linear Algebra"],
    ["94", "Art History"],
    ["94", "Operating Systems"],
    ["17", "Software Design"],
    ["58", "Mechanics"],
    ["58", "Economics"],
    ["17", "Linear Algebra"],
    ["17", "Political Science"],
    ["94", "Economics"]
]

print(find_pairs(student_course_pairs))
