class Calculation:
    def solve(self, n, matrix):
        res = []
        taken_task = set()
        current = []

        def backtrack(emp_id):
            if emp_id == n:
                res.append(list(current))
                return
            
            
            for task_idx in range(n):
                
                if task_idx not in taken_task and matrix[emp_id][task_idx] == 0:
                    
                   
                    taken_task.add(task_idx)
                    current.append((emp_id + 1, task_idx + 1)) 

                    
                    backtrack(emp_id + 1)

                    
                    current.pop()
                    taken_task.remove(task_idx)

        backtrack(0)
        return res


n = 3
matrix = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 0]
]

calc = Calculation()
all_solutions = calc.solve(n, matrix)


for sol in all_solutions:
    
    for emp, task in sol:
        print(f"Employee {emp} : Task {task}")
    print()