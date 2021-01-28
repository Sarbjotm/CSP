A = [1,2,3,4,5,6]
B = [1,2,3,4,5,6]
C = [1,2,3,4,5,6]
D = [1,2,3,4,5,6]
E = [1,2,3,4]
F = [1,2,3,4]

ASolution = []
BSolution = []
CSolution = []
DSolution = []
ESolution = []
FSolution = []
bFirstRun = 1

numSolutions = 0
numFailures = 0

for a in A:
    if( a == 1):
        print("A=" + str(a) + " Failure!")
        numFailures += 1
        continue
    else:
        bFirstRun = 1
        print("A=" + str(a), end ="")
    for b in B:
        if(((abs(a - b) != 1) or (b % 2 == 0)) and (bFirstRun == 1)):
            bFirstRun = 0
            cFirstRun = 1
            print(" B=" + str(b) + " Failure!")
            numFailures += 1
            continue
        elif ((abs(a - b) != 1) or (b % 2 == 0)):
            print("    B=" + str(b) + " Failure!")
            numFailures += 1
            cFirstRun = 1
            continue
        else:
            cFirstRun = 1
            if(bFirstRun == 1):
                bFirstRun = 0
                cFirstRun = 1
                print(" B=" + str(b), end="")
            else:
                print("    B=" + str(b), end ="")

        #a==c or b+c!=4
        for c in C:
            if(((a==c) or (b+c != 4)) and (cFirstRun == 1)):
                cFirstRun = 0
                print(" C=" + str(c) + " Failure!")
                numFailures += 1
                continue
            elif((a==c) or (b+c != 4)):
                print("        C=" + str(c) + " Failure!")
                numFailures += 1
                continue
            else:
                dFirstRun = 1
                if(cFirstRun == 1):
                    cFirstRun = 0;
                    print(" C=" + str(c), end="")
                else:
                    print("        C=" + str(c), end ="")  

           

            for d in D:
                if( ((b+d)%3 != 0) or (d % 2 != 0)) and (dFirstRun == 1):
                    dFirstRun = 0
                    numFailures += 1
                    print(" D=" + str(d) + " Failure!")
                    continue
                elif( ((b+d)%3 != 0) or (d % 2 != 0)):
                    numFailures += 1
                    print("            D=" + str(d) + " Failure!")
                    continue
                else:
                    eFirstRun = 1
                    if(dFirstRun == 1):
                        dFirstRun = 0;
                        print("            D=" + str(d), end="")
                    else:
                        print("            D=" + str(d), end ="")   

                for e in E:
                    if( ((c < e) or ((d-e)%2 != 1)) and (eFirstRun == 1) ):
                        eFirstRun = 0
                        numFailures += 1    
                        print(" E=" + str(e) + " Failure!")
                        continue
                    elif((c < e) or ((d-e)%2 != 1)):
                        numFailures += 1
                        print("                E=" + str(e) + " Failure!")
                        continue
                    else:
                        fFirstRun = 1
                        if(eFirstRun == 1):
                            eFirstRun = 0
                            print(" E=" + str(e), end="")
                        else:
                            print("                E=" + str(e), end ="")

                    for f in F:
                        if( ((e >= f) or ( (e+f) % 2 != 0)) and (fFirstRun == 1)):
                            fFirstRun = 0
                            numFailures += 1
                            print(" F=" + str(f) + " Failure!")
                            continue
                        elif ((e >= f) or ( (e+f) % 2 != 0)):
                            numFailures += 1
                            print("                    F=" + str(f) + " Failure!")
                            continue
                        else:
                            ASolution.append(a)
                            BSolution.append(b)
                            CSolution.append(c)
                            DSolution.append(d)
                            ESolution.append(e)
                            FSolution.append(f)
                            numSolutions += 1
                            if(fFirstRun == 1):
                                fFirstRun = 0
                                print(" F=" + str(f) + " Solution!")
                            else:
                                print("                    F=" + str(f) + " Solution!")


print("\n \nNumber of Failures: " + str(numFailures) + "\nNumber of Solutons: " + str(numSolutions))
print("Solutions Found: ")
for i in range(0,len(ASolution)):
    print("A=" + str(ASolution[i]) + " B=" + str(BSolution[i]) + " C=" + str(CSolution[i]) + " D=" + str(DSolution[i]) + " E=" + str(ESolution[i]) + " F=" + str(FSolution[i]))