# Name: Conor Smith
# Date: 6/21/21
# Description: Imports the statistics module. Creates student objects which are described by names and grades. Then uses
# a function to take the grades of the student objects and runs statistical evaluations on them to find their mean,
# median, and mode.

import statistics #imports the statistic module that lets us use pre coded functions for mean median and mode

class Student:
    """creates student objects initiated by a name and a grade, names and grades are private data members"""
    def __init__(self, name, grade):
        self._name = name
        self._grade = grade

    def get_grade(self): #get method for grades
        return self._grade

def basic_stats(student_list):
    """uses for loop to iterate over student list and takes grades from student objects and finds mean, median, and mode"""
    grade = []
    for i in student_list:
        grade.append(i._grade)

    return statistics.mean(grade), statistics.median(grade), statistics.mode(grade)

#s1 = Student("Kyoungmin", 73)
#s2 = Student("Mercedes", 74)
#s3 = Student("Avanika", 78)
#s4 = Student("Marta", 74)


#student_list = [s1, s2, s3, s4]
#print(basic_stats(student_list))