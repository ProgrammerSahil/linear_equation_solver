eq1 = list(input("Enter a, b and c of the equation ax+by+c=0 : ").split())
eq2 = list(input("Enter A, B and C of the equation Ax+By+C=0 : ").split())

#SEPARATE BY SPACE OBVS.
#WE WILL USE THE ELIMINATION METHOD TAUGHT IN SCHOOL

class equation:
    def __init__(self, eq1, eq2):
        self.eq1 = eq1
        self.eq2 = eq2
        self.result_list = []
    def step1(self):		# we will solve for y
        #making same coefficient for a and A
        lcm_for_a = float(self.eq1[0])*float(self.eq2[0])
        prev1 = float(self.eq1[0])
        prev2 = float(self.eq2[0])
        self.eq1[0] = self.eq2[0] = lcm_for_a
        self.eq1[1], self.eq1[2] = float(self.eq1[1])*prev2, float(self.eq1[2])*prev2
        self.eq2[1], self.eq2[2] = float(self.eq2[1])*prev1, float(self.eq2[2])*prev1

    def step2(self):
        #moving c and C to the other side of the equation and,
        #subtracting b and B
        self.eq1[2], self.eq2[2] = -self.eq1[2], -self.eq2[2]
        #after this, the equations are in the form ax+by=-c respectively

        self.result_list.append(self.eq1[1]-self.eq2[1])
        self.result_list.append(self.eq1[2]-self.eq2[2])

    def step3(self):
        var_y = self.result_list[1]/self.result_list[0]
        var_x = (self.eq1[2]-(self.eq1[1]*var_y))/self.eq1[0]
        ret_list = [var_x, var_y]
        return ret_list

new = equation(eq1, eq2)
new.step1()
new.step2()
x = new.step3()
print(x)
