import pytest 
import requests
from main import solution, vote, check_age

@pytest.mark.parametrize(
    'a,b,c,expected',
    (
        [1, 8, 15, (-3.0,  -5.0)],
        [1, -13, 12, (12.0, 1.0)],
        [-4, 28, -49, (3.5)],
        [1, 1, 1, 'корней нет']
     )
)
def test_solution(a, b, c, expected):
    actual = solution(a, b, c)
    assert actual == expected
    
@pytest.mark.parametrize(
    'votes, max_times',
    (
        [[1,1,1,2,3], 1],
        [[1,2,3,2,2], 2]
    )
)
def test_vote(votes, max_times):
    assert vote(votes) == max_times

@pytest.mark.parametrize(
    'age, expected',
    (
        [10, 'Доступ запрещён'],
        [20, 'Доступ разрешён']
    )
)
def test_check_age(age, expected):
    result = check_age(age)
    assert result == expected
    