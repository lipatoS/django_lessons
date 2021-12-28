lst = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
for k, i in enumerate(lst):
    print([i[k] for i in lst])
