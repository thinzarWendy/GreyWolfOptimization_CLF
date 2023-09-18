import numpy 
def param(a):
    param = {0: [0, 1, 24]}
    return param.get(a,"noting")

def assignValue(pos):
    wolfPos = []
    for i in pos:
        print(i)
        print()
        wolfPos.append(i)
    return numpy.array(wolfPos)

def binerization(pos):
    k = 0
    h = 0
    for i in pos:
        h = 0
        for j in i:
            if (j <= 0.5):
                pos[k, h] = 0
            else:
                pos[k, h] = 1
            h+=1
        k+=1
    return pos

unc_details = param(0)
#print(unc_details[2])
lb = unc_details[0]
ub = unc_details[1]
dim = unc_details[2]
SearchAgents_no = 7
Iterations= 7
Alpha_pos=numpy.zeros(unc_details[2])
#print(Alpha_pos)

Positions=numpy.random.uniform(0,1,(SearchAgents_no,dim)) *(ub-lb)+lb  #(7,24)
#print(Positions)
#print(Positions[0,0])
#print(type(Positions))
#print(Positions.shape)
#print(Positions)
#print(2-(Iterations-1)*((2)/(Iterations)))

pos = binerization(Positions)
#print(pos.shape)
#print(pos)
#print(pos[1,:])

#wolfpos = assignValue(pos[1,:])
#print(wolfpos)
Convergence_curve=numpy.zeros(7) 
Convergence_curve[0]=0.2
print(Convergence_curve)