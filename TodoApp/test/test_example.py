import pytest


def test_equal_or_not_equal():
    assert 3 == 3


def test_is_instance():
    assert isinstance('This is a string.', str)
    assert not isinstance('10', int)


def test_boolean():
    validated = True
    assert validated is True
    assert ('hello' == 'world') is False


def test_type():
    assert type('hello' is str)
    assert type('world' is not int)


def test_greater_and_less_than():
    assert 3 > 2
    assert 10 < 11


def test_list():
    num_list = [1, 2, 3, 4, 5]
    any_list = [False, False]
    assert 1 in num_list
    assert 7 not in num_list
    assert all(num_list)
    assert not any(any_list)



class Student:
    def __init__(self, firstname: str, lastname: str, major: str, years: int):
        self.firstname = firstname
        self.lastname = lastname
        self.major = major
        self.years = years



@pytest.fixture
def default_employee():
    return Student(firstname='John', lastname='Doe', major='Computer Science', years=3)
        

def test_person_initialization(default_employee):
    assert default_employee.firstname == 'John', 'firstname should be John'
    assert default_employee.lastname == 'Doe', 'lastname should be Doe'
    assert default_employee.major == 'Computer Science'
    assert default_employee.years == 3