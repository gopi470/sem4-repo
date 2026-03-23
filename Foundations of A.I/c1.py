import heapq

class SearchProblem:
    def __init__(self,start,goal):
        self.start=start
        self.goal=goal
    def is_goal(self,state):
        return state==self.goal
    def neighbors(self,state):
        return neighbors(state)

class PriorityQ:
    def __init__(self):
        self.h=[]
        self._cnt=0
    def is_empty(self):
        return len(self.h)==0
    def add(self,priority,parent,state,g):
        self._cnt+=1
        heapq.heappush(self.h,(priority,self._cnt,parent,state,g))
    def remove(self):
        priority,_,parent,state,g=heapq.heappop(self.h)
        return priority,parent,state,g

def neighbors(state):
    r=c=0
    found=False
    for i in range(3):
        for j in range(3):
            if state[i][j]==0:
                r,c=i,j
                found=True
                break
        if found:
            break
    moves=[(-1,0),(1,0),(0,-1),(0,1)]
    res=[]
    for dr,dc in moves:
        nr,nc=r+dr,c+dc
        if 0<=nr<3 and 0<=nc<3:
            temp=[list(row) for row in state]
            temp[r][c],temp[nr][nc]=temp[nr][nc],temp[r][c]
            res.append(tuple(tuple(row) for row in temp))
    return res

def h_misplaced(state,goal):
    cnt=0
    for i in range(3):
        for j in range(3):
            if state[i][j]!=0 and state[i][j]!=goal[i][j]:
                cnt+=1
    return cnt

def h_manhattan(state,goal):
    pos={}
    for i in range(3):
        for j in range(3):
            pos[goal[i][j]]=(i,j)
    dist=0
    for i in range(3):
        for j in range(3):
            v=state[i][j]
            if v!=0:
                gi,gj=pos[v]
                dist+=abs(i-gi)+abs(j-gj)
    return dist

class Searcher:
    def __init__(self,problem):
        self.problem=problem

    def _priority(self,mode,g,h):
        if mode=="UCS":
            return g
        if mode=="GREEDY":
            return h
        return g+h

    def search(self,mode="ASTAR",heuristic=h_manhattan):
        for sol in self.search_solutions(mode,heuristic):
            return sol
        return None

    def search_solutions(self,mode="ASTAR",heuristic=h_manhattan):
        frontier=PriorityQ()
        start=self.problem.start
        frontier.add(self._priority(mode,0,heuristic(start,self.problem.goal)),None,start,0)
        best_g={start:0}
        while not frontier.is_empty():
            _,parent,state,g=frontier.remove()
            if self.problem.is_goal(state):
                yield self._reconstruct(parent,state)
            if state in best_g and g>best_g[state]:
                continue
            for ns in self.problem.neighbors(state):
                ng=g+1
                if ns in best_g and ng>=best_g[ns]:
                    continue
                best_g[ns]=ng
                h=heuristic(ns,self.problem.goal)
                f=self._priority(mode,ng,h)
                frontier.add(f,(state,parent),ns,ng)

    def step_paths(self,mode="ASTAR",heuristic=h_manhattan):
        frontier=PriorityQ()
        start=self.problem.start
        frontier.add(self._priority(mode,0,heuristic(start,self.problem.goal)),None,start,0)
        best_g={start:0}
        while not frontier.is_empty():
            _,parent,state,g=frontier.remove()
            yield self._reconstruct(parent,state)
            if state in best_g and g>best_g[state]:
                continue
            for ns in self.problem.neighbors(state):
                ng=g+1
                if ns in best_g and ng>=best_g[ns]:
                    continue
                best_g[ns]=ng
                h=heuristic(ns,self.problem.goal)
                f=self._priority(mode,ng,h)
                frontier.add(f,(state,parent),ns,ng)

    def _reconstruct(self,parent,state):
        path=[state]
        while parent is not None:
            prev,parent=parent
            path.append(prev)
        path.reverse()
        return path

def print_state(state):
    for row in state:
        print(" ".join(str(x) if x!=0 else "_" for x in row))
    print()

def main():
    start=((7,2,4),(5,6,0),(8,3,1))
    goal=((1,2,3),(4,5,6),(7,8,0))
    problem=SearchProblem(start,goal)
    searcher=Searcher(problem)
    heuristic=h_manhattan

    path=searcher.search("UCS",heuristic)
    if path:
        print("UCS")
        for i,s in enumerate(path):
            print("Step",i)
            print_state(s)

    path=searcher.search("GREEDY",heuristic)
    if path:
        print("GREEDY")
        for i,s in enumerate(path):
            print("Step",i)
            print_state(s)

    path=searcher.search("ASTAR",heuristic)
    if path:
        print("A*")
        for i,s in enumerate(path):
            print("Step",i)
            print_state(s)

if __name__=="__main__":
    main()