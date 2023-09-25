# Prompt the user for input and create the list
n = int(input("Enter the length of the list: "))
lst = [int(input(f"Enter the element {i + 1}: ")) for i in range(n)]

# Sort the list
lst.sort()

# Calculate the differences between consecutive elements
gaps = [lst[i + 1] - lst[i] for i in range(len(lst) - 1)]

# Find the two shortest distances
sorted_gaps = sorted(gaps)
shortest_distances = sorted_gaps[:2]

# Print the results
print("------------------------------------------")
print(f"Sorted list is: {lst}")
for distance in shortest_distances:
    indices = [i for i, gap in enumerate(gaps) if gap == distance]
    for index in indices:
        print(f"The 2 shortest points are: {lst[index]} & {lst[index + 1]}\tDistance: {distance}")
        print("------------------------------------------")
