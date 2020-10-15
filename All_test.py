import pytest
import System
import Staff
import User
import json
import Professor
import Student

def test_login(grading_system):
    username = 'cmhbf5'
    password =  'bestTA'
    grading_system.login(username,password)
    grading_system.reload_data()
    users = grading_system.users
    if users[username]['role'] != 'ta':
        assert False

#Tests to see if program can handle a wrong password
def test_check_password(grading_system):
    name = 'cmhbf5'
    pword = 'bestTA'
    grading_system.login(name,pword)
    grading_system.check_password(name, pword)
    grading_system.reload_data()
    users = grading_system.users
    if users[name]['password'] != pword:
        assert False

def test_change_grade(grading_system):
    grading = Staff.Staff()
    name = 'akend3'
    course = 'comp_sci'
    assignment = 'assignment1'
    grade = 10
    grading_system.login('cmhbf5', 'bestTA')
    grading_system.usr.change_grade(name, course, assignment, grade)
    grading_system.reload_data()
    users = grading_system.users
    if users[name]['courses'][course][assignment]['grade'] != grade:
        assert False

def test_create_assignment(grading_system):
    grading = Staff.Staff()
    course = 'comp_sci'
    assignment = 'assignment10'
    dueDate = '9/9/9999'
    grade = 10
    grading_system.login('cmhbf5', 'bestTA')
    grading_system.usr.create_assignment(assignment, dueDate, course)
    grading_system.reload_data()
    courses = grading_system.courses
    if courses[course]['assignments'][assignment]['due_date'] != dueDate:
        assert False

def test_add_student(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    grading = Professor.Professor('goggins', users, courses)
    name = 'Adrien'
    course = 'comp_sci'
    grading_system.login('goggins', 'augurrox')
    grading_system.usr.add_student(name, course)
    grading_system.reload_data()

def test_drop_student(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    grading = Professor.Professor('goggins', users, courses)
    name = 'akend3'
    course = 'databases'
    grading_system.login('goggins', 'augurrox')
    grading_system.usr.drop_student(name, course)
    grading_system.reload_data()
    for c in users[name]['courses']:
        if c == course:
            assert False

def test_submit_assignment(grading_system):
    users = grading_system.users
    courses = grading_system.courses
    name = 'hdjsr7'
    password = 'pass1234'
    course = 'databases'
    assignmentName = 'assignment1'
    submission = "i just submitted my assignment brooooo"
    submissionDate = '9/9/21'
    grading = Student.Student('hdjsr7', users, courses)
    grading_system.login(name, password)
    grading_system.usr.submit_assignment(course, assignmentName, submission, submissionDate)
    grading_system.reload_data()
    if users[name]['courses'][course][assignmentName]['submission'] != submission:
        assert False
    if users[name]['courses'][course][assignmentName]['submission_date'] != submissionDate:
        assert False

def test_check_ontime(grading_system):
    name = 'hdjsr7'
    password = 'pass1234'
    submissionDate = '9/9/21'
    dueDate = '8/1/20'
    grading_system.login(name, password)
    isOnTime = grading_system.usr.check_ontime(submissionDate, dueDate)
    if isOnTime == True:
        assert False

def test_check_grades(grading_system):
    users = grading_system.users
    name = 'hdjsr7'
    password = 'pass1234'
    course = 'databases'
    grading_system.login(name, password)
    grades = grading_system.usr.check_grades(course)
    for i in users[name]['courses'][course]['grade']:
        if i != grades[i]:
            assert False

def test_view_assignments(grading_system):
    courses = grading_system.courses
    name = 'hdjsr7'
    password = 'pass1234'
    course = 'databases'
    grading_system.login(name, password)
    assignments = grading_system.usr.view_assignments(course)
    for i in courses[course]['assignments']:
        if i != assignments[i]:
            assert False

def test_is_passing(grading_system):
    name = 'hdjsr7'
    password = 'pass1234'
    grading_system.login(name, password)
    isPassing = grading_system.usr.is_passing(course, assignment)
    if isPassing == False:
        assert False

def test_is_enrolled(grading_system):
    name = 'hdjsr7'
    password = 'pass1234'
    grading_system.login(name, password)
    isEnrolled = grading_system.usr.is_enrolled('cloud_computing')
    if isEnrolled == True:
        assert False

def test_drop_course(grading_system):
    name = 'hdjsr7'
    password = 'pass1234'
    course = 'cloud_computing'
    grading_system.login(name, password)
    grading_system.usr.drop_course(course)
    isEnrolled = grading_system.usr.is_enrolled(course)
    if isEnrolled == True:
        assert False

def test_add_course(grading_system):
    name = 'hdjsr7'
    password = 'pass1234'
    course = 'cloud_computing'
    grading_system.login(name, password)
    grading_system.usr.drop_course(course)
    isEnrolled = grading_system.usr.is_enrolled(course)
    if isEnrolled == True:
        assert False

def test_view_classes(grading_system):
    courses = grading_system.courses
    name = 'hdjsr7'
    password = 'pass1234'
    grading_system.login(name, password)
    classes = grading_system.usr.view_classes()
    for i in courses[course]['courses']:
        if i != assignments[i]:
            assert False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
