lst = [1, 2]
print("lst", lst)
lst.append(3)
print("lst.append(3)", lst)
lst.append([4,5])
print("lst.append([4,5])", lst)
lst.clear()
print("lst.clear()", lst, "\n")

lst = [1,2,'a']
ab = lst.copy()
print("lst", lst)
print("lst.copy()", ab, "\n")

lst = [1,2,1,3,1]
print("lst", lst)
print("lst.count(1)", lst.count(1))
lst.extend(['a','b'])
print("lst.extend(['a','b'])", lst, "\n")

lst = ['a', 'b']
print("lst", lst)
lst.insert(1,2)     # imsert(index, value)
print("lst.insert(1,2)", lst)
lst.pop(1)  # remove item index 1
print("lst.pop(1)", lst)
lst.remove('a')
print("lst.remove('a')", lst, "\n")

lst = [1, 2, 1, 3, 'a']
print("lst: ", lst)
lst.reverse()
print("lst.reverse()", lst)
lst.remove('a')
print("lst.remove('a')", lst)
lst.sort()
print("lst.sort()", lst)