tree = {
    'jonh' : ['alice','bob'],
    'alice' :['alexa','shri'],
    'alexa':[]
    
}


def descendents(tree,parent):
    descendents = []
    
    def des(parent):
        if parent in tree:
            for child in tree[parent]:
                descendents.append(child)
                des(child)
            

    des(parent)
    return descendents

descendent = descendents(tree , 'jonh')
print(descendent)