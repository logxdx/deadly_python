def merge_overlap_intervals(intervals):
    print("Intervals :",intervals)
    intervals.sort(key=lambda x: x[0])
    print("Sorted Intervals :",intervals)
    k=0
    l,r=1,len(intervals)
    while l<r:
        interval=intervals[l]
        if interval[0] <= intervals[k][1]:
            intervals[k] = [intervals[k][0], max(intervals[k][1], interval[1])]
            intervals.remove(interval)
            r-=1
        else:
            l+=1
            k+=1
    return intervals


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_overlap_intervals(intervals))
intervals = [[1,4],[4,5]]
print(merge_overlap_intervals(intervals))
