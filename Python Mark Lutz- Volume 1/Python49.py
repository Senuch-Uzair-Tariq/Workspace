local={1.23};
print(local)
local.add((1,2,3))
print(local)
print((1,2,3) in local)
print(local.pop())
print(local)
tuple=local.pop()
print(tuple)
print(local)
print(tuple[1])