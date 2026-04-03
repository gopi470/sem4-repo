from typing import List

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        # Sorting descending allows the pruning condition to hit sooner
        jobs.sort(reverse=True)
        worker_loads = [0] * k
        best_result = sum(jobs)
        
        def backtrack(job_idx):
            nonlocal best_result
            
            # Base Case: All jobs assigned
            if job_idx == len(jobs):
                best_result = min(best_result, max(worker_loads))
                return
            
            curr_job = jobs[job_idx]
            
            for i in range(k):
                # Pruning 1: If current assignment is already worse than 
                # our best_result, there is no point in continuing this path.
                if worker_loads[i] + curr_job >= best_result:
                    continue
                
                # Assign the job to worker i
                worker_loads[i] += curr_job
                backtrack(job_idx + 1)
                # Backtrack: remove the job to try the next worker
                worker_loads[i] -= curr_job
                
                # Pruning 2: Symmetry Breaking
                # If worker i had 0 load, then worker i+1 (and others) are 
                # also empty. Trying them would just repeat the same work.
                if worker_loads[i] == 0:
                    break
                    
        backtrack(0)
        return best_result