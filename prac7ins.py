#prac 7 INS
def main():
    print ("enter Q")
    q=input()
    print ("enter a")
    a=input()
    print ("enter xa")
    xa=input()
    print ("enter xb")
    xb=input()
    ya=pow(int(a),int(xa))%int(q)
    print ("ya = " + str(ya))
    yb=pow(int(a),int(xb))%int(q)
    print ("yb = " + str(yb))
    print ("////////////////////////session key//////////////////////////////")
    ka = pow(int(yb),int(xa))% int(q)
    print ("ka = " + str(ka))
    kb = pow(int(ya),int(xb))% int(q)
    print ("kb = " + str(kb))
main()    