What is the Big-O notation running time of the following functions:

```
def cost(n):
    out = 1
    for i in range(n):
        out = out * 2
    return out
```

```
def cost(n):
    out = 1
    for i in range(n):
        next = 1
        for j in range(i):
           next = next + next
        out = out + next
    return out
```

```
def cost(n):
    if n == 0:
        return 1
    else:
        return cost(n-1) + cost(n-1)
```

```
def cost(n):
    if n == 0:
        return 1
    else:
        return 2*cost(n-1)
```

```
def cost(n):
    return 2*n
```

