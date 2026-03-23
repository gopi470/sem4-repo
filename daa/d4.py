import math

# Function to calculate Euclidean distance
def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Brute force for base cases (n=2 or n=3)
def brute_force(P):
    min_d = float('inf')
    res_pair = (None, None)
    for i in range(len(P)):
        for j in range(i + 1, len(P)):
            d = dist(P[i], P[j])
            if d < min_d:
                min_d = d
                res_pair = (P[i], P[j])
    return min_d, res_pair

def closest_pair_recursive(X, Y):
    n = len(X)
    
    # Base cases: If 2 or 3 points, solve directly
    if n <= 3:
        return brute_force(X)
    
    # Divide: Find middle index
    mid = n // 2
    mid_point = X[mid]
    
    # Split sorted Y array into left and right based on X-midpoint
    Y_left = []
    Y_right = []
    for p in Y:
        if p[0] <= mid_point[0]:
            Y_left.append(p)
        else:
            Y_right.append(p)
            
    # Conquer: Recursive calls for left and right halves
    dl, pair_l = closest_pair_recursive(X[:mid], Y_left)
    dr, pair_r = closest_pair_recursive(X[mid:], Y_right)
    
    # Find the smaller of the two distances
    if dl < dr:
        d, best_pair = dl, pair_l
    else:
        d, best_pair = dr, pair_r
        
    # Combine: Check the strip S
    # Points in Y whose x-coordinates are within range [mid.x - d, mid.x + d]
    S = [p for p in Y if abs(p[0] - mid_point[0]) < d]
    
    # Check each point in the strip against the next 7 points
    for i in range(len(S)):
        # Inner loop runs at most 7 times as per the video proof
        for j in range(i + 1, min(i + 8, len(S))):
            d_strip = dist(S[i], S[j])
            if d_strip < d:
                d = d_strip
                best_pair = (S[i], S[j])
                
    return d, best_pair

# Main execution
Points = [(2,3), (12,30), (40,50), (5,1), (12,10)]

# Pre-sorting P into X and Y as required by the algorithm
X = sorted(Points, key=lambda p: p[0])
Y = sorted(Points, key=lambda p: p[1])

min_dist, pair = closest_pair_recursive(X, Y)

print(f"Closest Pair = {pair[0]} and {pair[1]}")
print(f"Minimum Distance = {min_dist:.2f}")