class Queue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        if len(self.items)==0:
            return True
        else:
            return False
    def add(self,x):
        self.items.append(x)
    def remove(self):
        x=self.items[0]
        del self.items[0]
        return x


CAP=(8,5,3)

def next_states(st):
    out=[]
    jars=list(st)
    for i in range(3):
        for j in range(3):
            if i!=j:
                if jars[i]>0 and jars[j]<CAP[j]:
                    amt=min(jars[i],CAP[j]-jars[j])
                    ns=jars[:]
                    ns[i]=ns[i]-amt
                    ns[j]=ns[j]+amt
                    out.append(tuple(ns))
    return out

def goal_test(st):
    goal_list=[(4,4,0),(4,1,3),(4,3,1),(1,4,3)]
    if st in goal_list:
        return True
    else:
        return False

def decant_bfs(start_st):
    frontier=Queue()
    frontier.add(start_st)
    prev={}
    prev[start_st]=None
    while frontier.is_empty()==False:
        cur_st=frontier.remove()
        if goal_test(cur_st):
            return prev,cur_st
        moves=next_states(cur_st)
        for ns in moves:
            if ns not in prev:
                prev[ns]=cur_st
                frontier.add(ns)
    return None,None


def show_path(prev,end_st):
    seq=[]
    t=end_st
    while t!=None:
        seq.append(t)
        t=prev[t]
    seq.reverse()
    for st in seq:
        print(st)

def decant_goal():
    start_st=(8,0,0)
    prev,goal_st=decant_bfs(start_st)
    if goal_st==None:
        print("No solution")
    else:
        show_path(prev,goal_st)


def decant_goal_yield():
    start_st=(8,0,0)
    frontier=Queue()
    frontier.add(start_st)
    prev={}
    prev[start_st]=None
    while frontier.is_empty()==False:
        cur_st=frontier.remove()
        if goal_test(cur_st):
            show_path(prev,cur_st)
            return
        moves=next_states(cur_st)
        for ns in moves:
            if ns not in prev:
                prev[ns]=cur_st
                frontier.add(ns)

print("Using decant_goal():")
decant_goal()
print("\nUsing decant_goal_yield():")
decant_goal_yield()
