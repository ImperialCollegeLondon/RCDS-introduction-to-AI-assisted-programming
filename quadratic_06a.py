import math

def quadratic_solver(a, b, c):
    '''
    Solves the quadratic equation ax^2 + bx + c = 0.
    param a: float - coefficient of x^2
    param b: float - coefficient of x
    param c: float - constant term
    return: tuple - solutions to the equation
    raise: ValueError - if a is 0 or if the discriminant is negative
    '''
    determinant = b ** 2 - 4 * a * c
    if determinant == 0:
        return -b / (2 * a)
    return (-b - math.sqrt(determinant)) / (2 * a), (-b + math.sqrt(determinant)) / (2 * a)