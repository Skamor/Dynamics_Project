from math import sin, cos, radians, sqrt

ANGLE = 80 # in degrees
LENGHT = 0.2286 # 9 inches in metres
GRAVITY = 9.81
SPRING_CONSTANT = 1225.89 # 7 pounds/inch in N/m
kINETIC_COEFFICIENT = 0.2 #need to get this measured


# have to do a quadratic so these are to split up the math
def get_a(mass):
    return 0.5*SPRING_CONSTANT

def get_b(mass):
    return mass*GRAVITY*sin(radians(ANGLE))*-1 + kINETIC_COEFFICIENT*mass*GRAVITY*cos(radians(ANGLE))

def get_c(mass):
    return (mass*GRAVITY*sin(radians(ANGLE))*-1 + kINETIC_COEFFICIENT*mass*GRAVITY*cos(radians(ANGLE)))*LENGHT

# finds the compression in the spring
def find_x(mass):
    a = get_a(mass)
    b = get_b(mass)
    c = get_c(mass)
    final = []
    try:
        x = (-1*b + sqrt(b**2 - 4*a*c))/(2*a)
        final.append(x)
    except:
        final.append("1 did not work")
    try:
        x2 = (-1*b - sqrt(b**2 - 4*a*c))/(2*a)
        final.append(x2)
    except:
        final.append("2 did not work")

    return final

#finds the height attained by the mass depending on the compression of the spring
def find_l(mass):
    x = find_x(mass)[0]
    l = (0.5*SPRING_CONSTANT*x**2 -x*(kINETIC_COEFFICIENT*mass*GRAVITY*cos(radians(ANGLE)) + mass*GRAVITY*sin(radians(ANGLE))))/(kINETIC_COEFFICIENT*mass*GRAVITY*cos(radians(ANGLE)) + mass*GRAVITY*sin(radians(ANGLE)))
    return l

#obtains the info that is inputed
info = []
lines = []
def get_info():
    global info
    global lines
    with open("input.txt", "r") as file:
        info = file.read().split("\n")
        lines = [line.split(" ") for line in info]

get_info()
print(lines)

# calculates height for all masses
def calc_all():
    theory_height = []
    for attempt in lines:
        print(attempt[1])
        theory_height.append(find_l(float(attempt[1])))
    return theory_height

# gathers all data together and calculates errors
def create_table(theory):
    table = []
    for i in range(len(theory)):
        table.append([])
    for i in range(len(lines)):
        table[i].append(float(lines[i][0]))
        table[i].append(theory[i])
        table[i].append(abs(float(lines[i][0])-theory[i])/theory[i]*100)
    return table


first = find_l(1)
second = find_l(10)
third = find_l(100)
print(first, second, third)
heights = calc_all()
table = create_table(heights)
print(table)