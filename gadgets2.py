

def depthling(input):

    if type(input[0]) == type(0):
        return (input[:])
    return ([depthling(x) for x in input])

