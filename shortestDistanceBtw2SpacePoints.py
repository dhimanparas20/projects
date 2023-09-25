lst = []
gap = []

n = int(input("Enter the length of list: "))
for i in range(0,n):
    inp = int(input(f"Enter the element {i+1}: "))
    lst.append(inp)

def sort (lst):
    ln = len(lst)
    for i in range(0,ln):
        for j in range(0,ln):
            if lst[i] < lst[j]:
                tmp = lst[j]
                lst[j] = lst[i]
                lst[i] = tmp
    return lst

lst = sort(lst)
print("------------------------------------------")
print(f"Sorted list is: {lst}")

for i in range(0,len(lst)):
    if i+1 < len(lst):
      gap.append((lst[i+1]-lst[i]))
      #print(f"{lst[i+1]}-{lst[i]}= {lst[i+1]-lst[i]}")

for i in range(0,len(lst)):
    if i+1 < len(lst):
      if lst[i+1]-lst[i] == sort(gap)[i]:
          print(f"The 2 shortest points are: {lst[i+1]}&{lst[i]}\tDistance: {sort(gap)[i]}")      
          print("------------------------------------------")
