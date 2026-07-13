# -------------------------------------------Arithematic Operator-------------------------------------------
# +,-,/,*
# Examples
from encodings.punycode import T

print(6 + 1)  # -> Addition Arthematic operator
print(6 - 1)  # -> Subtraction Arthematic operator
print(6 / 1)  # -> Division Arthematic operator
print(6 * 1)  # -> Multilication  Arthematic operator


# -------------------------------------------Assignment Operator-------------------------------------------
# =,+=,-=,etc
a = 3  # 3 is assigned to variable a
a += 4  # 4 is added to a's previous value and assigned to a :- a=3+4
a -= 1  # 1 is subracted to a's previous value and assigned to a :- a=7-1


# -------------------------------------------Comparison Operator-------------------------------------------
# ==,!=,>=,<= , <,> etc
v1 = 10
v2 = 20
result = v1 == v2
print(result)  # Will compare v1 with v2 if equals it return true else return false
result = v1 != v2
print(result)  # Will compare v1 with v2 if not-equals it return true else return false
result = v1 <= v2
print(
    result
)  # Will compare v1 with v2 if equals or v1 is less than v2  it return true else return false
result = v1 >= v2
print(
    result
)  # Will compare v1 with v2 if equals or v1 is greator than v2  it return true else return false
result = v1 < v2
print(
    result
)  # Will compare v1 with v2 if  v1 is less than v2  it return true else return false
result = v1 > v2
print(
    result
)  # Will compare v1 with v2 if  v1 is greator than v2  it return true else return false


# -------------------------------------------logical operators-------------------------------------------
# and , or , not
e = True or False  # any one of option is True mean it return True
print(e)
e = True and True  # any one of option is False mean it return False
e = not e  # it just reverse the value True to flase and False to true
