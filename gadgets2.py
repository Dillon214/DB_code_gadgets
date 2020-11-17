
#depthling is meant to clone an array or array of arrays into a new variable. This probably exists as some command, but I wanted to make it anyways bacause I was sick of my variables changing whe they weren't supposed to. 
def depthling(input):

    if type(input[0]) == type(0):
        return (input[:])
    return ([depthling(x) for x in input])









