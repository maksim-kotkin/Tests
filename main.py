def discriminant(a, b, c):
   return b ** 2 - 4 * a * c

def solution(a, b, c):
    if discriminant(a,b,c) < 0:
        return ('корней нет')
    elif discriminant(a,b,c) == 0:
        x = -b / (2 * a)
        return (x)
    elif discriminant(a,b,c) > 0:
        x_1 = (-b + discriminant(a,b,c) ** 0.5 )/ (2 * a)
        x_2 = (-b - discriminant(a,b,c) ** 0.5) / (2 * a)
        return (x_1, x_2)

def vote(votes):
    count = {}
    times = -1
    for a in votes:
        if count.get(a) is None:
            count[a] = 1
        else:
            count[a] += 1
        if count[a] > times:
            times = count[a]
            max_times = a
    return max_times


def check_age(age: int):

    if age >= 18:
        result = 'Доступ разрешён'
    else:
        result = 'Доступ запрещён'

    return result

    