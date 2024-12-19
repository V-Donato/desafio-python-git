import sys

def soma(primeiro, segunda, terceiro):
    print(primeiro + segunda + terceiro)

def mult(pri, sec, terc):
    print(pri * sec * terc)
    
if (sys.argv[1] == "+"):
    soma(int(sys.argv[2]), int(sys.argv[3]),int(sys.argv[4]))
    
elif (sys.argv[1] == "x"):
    mult(int(sys.argv[2]), int(sys.argv[3]),int(sys.argv[4]))   
.