

def inputFile(filename):
    rf = open(filename, 'r')
    m = int(rf.readline())
    query = []
    for i in range(m):
        sentence = rf.readline().strip('\n ').split(' ')
        # sentence = sentence.remove("OR")
        query.append(sentence)

    kb = []
    n = int(rf.readline())
    for i in range(n):
        sentence = rf.readline().strip('\n ').split(' ')
        kb.append(sentence)

    print(query, kb)
    input()
    rf.close()
    return

def checkEliminate(literal1, literal2):
    if literal1 == literal2:
        return False
    else:
        if len(literal1) == len(literal2):
            return False
        else:
            print(literal1[-1:1])
            print(literal2[-1:-2])
            return True


if __name__ == '__main__':
    # inputFile('./Input/input1.txt')
    print(checkEliminate('A','-B'))