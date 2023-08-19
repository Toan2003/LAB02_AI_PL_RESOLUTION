import copy

def inputFile(filename):
    rf = open(filename, 'r')
    m = int(rf.readline())
    query = []
    for i in range(m):
        sentence = rf.readline().strip('\n ').split(' ')
        # remove OR
        while 'OR' in sentence:
            sentence.remove('OR')
        # ----------------------------------------------------------------
        query.append(sentence)

    kb = []
    n = int(rf.readline())
    for i in range(n):
        sentence = rf.readline().strip('\n ').split(' ')
        # remove OR
        while 'OR' in sentence:
            sentence.remove('OR')
        # ----------------------------------------------------------------
        kb.append(sentence)
    # print(query, kb)
    rf.close()
    return m, n, query, kb

def checkIfLiteralIsOpposite(literal1, literal2):
    if literal1 == literal2:
        return False
    else:
        if len(literal1) == len(literal2):
            return False
        else:
            if literal1[-1:] == literal2[-1:]:
                return True
            return False

# def checkIfLiteralIsSimilar(literal1, literal2):
#     if literal1 == literal2:
#         return True
#     else:
#         return False

def returnOppositeQuery(query):
    result = []
    for clause in query:
        temp =[]
        if (len(clause) == 1):
            if len(clause[0]) == 2:
                temp.append(clause[0][1])
            else:
                temp.append('-'+clause[0][0])
            result.append(temp)
        else:
            for subClause in clause:
                temp =[]
                if len(subClause) == 2:
                    temp.append(subClause[1])
                else:
                    temp.append('-'+subClause[0])
                result.append(temp)
    # print(result)
    # input()
    return result

def checkIfSimilarClause(clause1, clause2):
    if len(clause1) != len(clause2):
        return False
    for i in range(0, len(clause1)):
        if clause1[i] != clause2[i]:
            return False
    return True 

def PLResolve(clause1, clause2):
    clause1 = copy.deepcopy(clause1)
    clause2 = copy.deepcopy(clause2)
    canMakeNew = False
    new = None
    for i in range(len(clause1)):
        for j in range(len(clause2)):
            if checkIfLiteralIsOpposite(clause1[i], clause2[j]):
                canMakeNew = True
                clause1.pop(i)
                clause2.pop(j)
                new = clause1 + clause2
                break
        if canMakeNew:
            break
    # print(new)
    if new == None or new == []:
        return new
    # check if dump clause
    for i in range(len(new)):
        for j in range(i+1,len(new)):
            if checkIfLiteralIsOpposite(new[i], new[j]):
                new = None
                return new
    # check if clause contains 2 similiar literals
    new = sorted(list(set(new)), key=lambda sub:sub[-1])
    return new

def PLResolution(kb, query):
    query = returnOppositeQuery(query)
    clauses =kb + query
    # print(clauses)
    # input()
    new = []
    while True:
        tempNew = []
        for i in range(len(clauses)):
            for j in range(i+1, len(clauses)):
                resolve = PLResolve(clauses[i],clauses[j])
                if resolve == []:
                    tempNew.append(resolve)
                    new.append(tempNew)
                    # print(new)
                    # print('----------------------------------------------------------------')
                    # print(clauses)
                    # input()
                    return 'YES', new
                if resolve != None:
                    isSimilar = False
                    for clause in clauses:
                        if checkIfSimilarClause(clause, resolve):
                            isSimilar = True
                            break
                    for clause in tempNew:
                        if checkIfSimilarClause(clause, resolve):
                            isSimilar = True
                            break
                    if isSimilar == False:
                        tempNew.append(resolve)
        if tempNew == []:
            new.append(tempNew)
            return "NO", new
        new.append(tempNew)
        clauses.extend(tempNew)
        # print(new)
        # print('----------------------------------------------------------------')
        # print(clauses)
        # input()

def outPut(link,new, result):
    wf = open(link, 'w')
    for n in new:
        wf.write(str(len(n))+'\n')  
        for i in n:
            if i == []:
                wf.write('{}' +'\n')
                break
            wf.write(i[0])
            for j in range(1,len(i)):
                wf.write(' OR ' + i[j])
            wf.write('\n')
    wf.write(str(result))

def interact():
    inp = input("Enter your file name: (example: path/input1.txt) ")
    out = input("Enter your file name: (example: path/output1.txt) ")
    # inp = './Input/' + inp
    # out = './Output/' + out
    # print(inp, out) 
    return inp, out

if __name__ == '__main__':
    inp, out = interact()
    m,n,query,kb = inputFile(inp)
    result, new = PLResolution(kb,query)
    outPut(out,new, result)
    print(result,new)
    # clause2 = [['C'],['A','-B'],['-C','A']]
    # print(returnOppositeQuery(clause2))
    # new = PLResolve(clause1,clause2)
    # print('check')
    # print(new)
