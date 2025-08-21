
  # =============================hackathon_3 task ====================

def find_missing_ranges(frames: list[int]) -> dict:
# ==================this for sorting if the list unordered ==================
    n = len(frames)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if frames[j] < frames[min_index]:
                min_index = j
        frames[i], frames[min_index] = frames[min_index], frames[i]
# ==================this for sorting if the list unordered ==================

    gaps = []
    missing_count = 0
    longest_gap = None
    longest_size = 0
    #================= for detecting gaps ==================
    for i in range(n - 1):
        current = frames[i]
        next_val = frames[i + 1]

        if next_val - current > 1:
            start = current + 1
            end = next_val - 1
            gaps.append([start, end])

    #================= for detecting gaps ==================
          

    #=================count the frames in the gap============      
            gap_size = end - start + 1
            missing_count += gap_size
    #=================count the frames in the gap============      

# ===================cheack the longest gap ==============
            if gap_size > longest_size:
                longest_size = gap_size
                longest_gap = [start, end]
# ===================cheack the longest gap ==============


    return {
        "gaps": gaps,
        "longest_gap": longest_gap,
        "missing_count": missing_count
    }


frames = [1, 2, 3, 5, 6, 10, 11, 16]
print(find_missing_ranges(frames))



# =============================hackathon_3 task ====================
