
#depthling is meant to clone an array or array of arrays into a new variable. This probably exists as some command, but I wanted to make it anyways bacause I was sick of my variables changing whe they weren't supposed to. 
def depthling(input):

    if type(input[0]) == type(0):
        return (input[:])
    return ([depthling(x) for x in input])


#addtogether takes two arrays or arrays of arrays with the same structure and adds together all elements.
#an example input pair of [1,2,3] and [1,3,3] would yield a result of [2,5,6]
def addtogether(input1, input2):
    if type(input1[0]) == type(0):

        return ([input1[x] + input2[x] for x in range(len(input1))])
    return ([addtogether(input1[x], input2[x]) for x in range(len(input1))])






