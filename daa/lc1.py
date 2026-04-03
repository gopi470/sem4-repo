from typing import List

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        jobs.sort(reverse=True)
        worker_loads = [0] * k
        best_result = sum(jobs)
        
        def backtrack(job_idx):
            nonlocal best_result
            
            if job_idx == len(jobs):
                best_result = min(best_result, max(worker_loads))
                return
            
            curr_job = jobs[job_idx]
            
            for i in range(k):
                if worker_loads[i] + curr_job >= best_result:
                    continue
                
                worker_loads[i] += curr_job
                backtrack(job_idx + 1)
                worker_loads[i] -= curr_job
                
                if worker_loads[i] == 0:
                    break
                    
        backtrack(0)
        return best_result