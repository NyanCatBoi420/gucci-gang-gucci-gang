# this is just some code to make vector life easier
import math

def dot(v1,v2): #regular computation of the dot product
    
    tot = 0
    for i in range(3):
        tot += v1[i] * v2[i] #going through each component in each vector assuming its in 3d, and multiplying them
        #dot product is a1*b1 + a2*b2 + a3*b3
        
    return tot #returning value



def geo_dot(magv1,magv2,θ1): #geometric compution of dot product with  2 magnitudes inputed and angle θ inputted(in degrees)
    
    θ = math.radians(θ1)#converting degrees to radians
    dottot = round(magv1 * magv2 * math.cos(θ),6) #actually calculating dot product by trigonometry

    return dottot #returning value

def geo_dot_rad(magv1,magv2,θ1): #geometric compution of dot product with  2 magnitudes inputed and angle θ inputted(in rad)
    
    dottot = round(magv1 * magv2 * math.cos(θ),6) #actually calculating dot product by trigonometry

    return dottot #returning value


def cross(v1,v2): #calculating the normal vector of two vectors
    
    VecMat = [["i","j","k"],v1,v2] #the typical way of calculating cross product is finding determinant of a matrix like this
    #^this might look like a bit of notational tomfoolery but thats ok because its indicative of what is going on
    
    CompX = VecMat[1][1]*VecMat[2][2] - VecMat[1][2]*VecMat[2][1] #calculating the horizontal component
    CompY = VecMat[1][0]*VecMat[2][2] - VecMat[1][2]*VecMat[2][0] #calculating the vertical component
    CompZ = VecMat[1][0]*VecMat[2][1] - VecMat[2][0]*VecMat[1][1] #calulating the outward component
    
    CrossVector = [CompX,CompY,CompZ] #creating the vector
    print(str(CompX) + "i+ " + str(CompY) + "j+ " + str(CompZ) + "k") #printing vector in unit vector form for the scrubs that read vectors like this
    
    return CrossVector #returning normal vector



def cart_3Dplane(vp,v1,v2): #converting vector form of plane to cartesian. vp is a position vector where as v1 and v2 are the two direction vectors to define all points
    
    constant = 0 #constant in cartesian starts at 0
    vn = cross(v1,v2)#finding normal vector
    
    for i in range(3):
        constant += vn[i]*vp[i] #finding constant by subbing in position vector
    Cartesian_Equation = str(vn[0]) + "x + " + str(vn[1]) + "y + " + str(vn[2]) + "z = " + str(constant) #creating cartesian equation
    
    return Cartesian_Equation

    
