tree  ={
    'home':{
        'about':{},
        'services':{
            'web development':{},
            'app development':{}
            
        },
        'blog':{
          'python':{},
          'java':{}  
            
        }
        
        
    }
}

def dfs(tree , target,path):
    for page , children in tree.items():
        path.append(page)
        if page == target:
            return True
        
        if dfs(children,target,path):
            return True
        path.pop()
        
    return False
    
    

target = 'java'    
    
path =[]
if dfs(tree,target,path):
    print(path)