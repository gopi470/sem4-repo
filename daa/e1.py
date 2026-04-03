def stable_matching(men_pref, women_pref):
    # 1. Initialize free men list
    free_men = list(men_pref.keys())
    
    # 2. Initialize data structures
    engaged = {}  # woman -> man
    proposed = {m: [] for m in men_pref}  # proposals made by each man
    rank = {}  # ranking of men for each woman

    # 3. Precompute ranking of men in each woman's preference list
    for w in women_pref:
        rank[w] = {man: i for i, man in enumerate(women_pref[w])}

    # 4. While there are free men
    while free_men:
        m = free_men.pop(0)

        for w in men_pref[m]:
            if w not in proposed[m]:
                proposed[m].append(w)

                # If woman is free
                if w not in engaged:
                    engaged[w] = m
                else:
                    current = engaged[w]
                    
                    # If woman prefers new man over current
                    if rank[w][m] < rank[w][current]:
                        engaged[w] = m
                        free_men.append(current)
                    else:
                        free_men.append(m)
                
                break  # move to next free man

    # 5. Return man -> woman mapping
    return {v: k for k, v in engaged.items()}




men = {
    "M1": ["W1", "W2", "W3"],
    "M2": ["W2", "W1", "W3"],
    "M3": ["W1", "W2", "W3"]
}

women = {
    "W1": ["M2", "M1", "M3"],
    "W2": ["M1", "M2", "M3"],
    "W3": ["M1", "M2", "M3"]
}

result = stable_matching(men, women)

print("Stable Matching:")
for m in sorted(result):
    print(f"{m} – {result[m]}")
