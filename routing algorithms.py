def star5_routing(source,dest):
    node = source
    route = [source[:]]
    for i in range(4,-1,-1):
        if source[i] != dest[i]:
            for j in range(i):
                if source[j] == dest[i]:
                    break
            if j!=0:
                node[j] = node[0]
                node[0] = dest[i]
                route.append(node[:])
            node[0] = node[i]
            node[i] = dest[i]
            route.append(node[:])
    return route

def hypercube_routing(n,source,target):
    node = source
    route = [source[:]]
    for i in range(n-1,-1,-1):
        if source[i] != target[i]:
            source[i] = target[i]
            route.append(source[:])
    return route

def karyncube_routing(n,k,source,target):
    node = source
    route = [source[:]]
    for i in range(n-1,-1,-1):
        start = source[i]
        dest = target[i]
        if start == dest:
            pass
        elif start > dest:
            clockwise = k-start + dest
            anticlock = start - dest
            if clockwise<=anticlock:
                for j in range(start+1,k):
                    source[i] = j
                    route.append(source[:])
                for j in range(dest+1):
                    source[i] = j
                    route.append(source[:])
            else:
                for j in range(start-1,dest-1,-1):
                    source[i] = j
                    route.append(source[:])
        elif start < dest:
            clockwise = dest - start
            anticlock = k-dest + start
            if clockwise<=anticlock:
                for j in range(start+1,dest+1):
                    source[i] = j
                    route.append(source[:])
            else:
                for j in range(start-1,-1,-1):
                    source[i] = j
                    route.append(source[:])
                for j in range(k-1,dest-1,-1):
                    source[i] = j
                    route.append(source[:])
    return route

#assuming node ((0,0,0),1) would be input as [0,0,0,1]
def cubeconncycle_routing(n,source,target):
    node = source
    route = [source[:]]
    cycle_pos = n-source[n]
    pos = n-source[n]
    while source[:-1] != target[:-1]:
        if pos == n:
            pos = 0
        if source[pos] != target[pos]:
            if pos >= cycle_pos:
                for i in range(cycle_pos+1,pos+1):
                    source[n] = n-i
                    route.append(source[:])
                cycle_pos = n-source[n]
                source[pos] = target[pos]
                route.append(source[:])
            else:
                for i in range(cycle_pos+1,n):
                    source[n] = n-i
                    route.append(source[:])
                for i in range(pos+1):
                    source[n] = n-i
                    route.append(source[:])
                cycle_pos = n-source[n]
                source[pos] = target[pos]
                route.append(source[:])
        pos+=1
    start = source[n]
    dest = target[n]
    if start == dest:
        return route
    elif start>dest:
        clockwise = n-start + dest
        anticlock = start - dest
        if clockwise<anticlock:
            for j in range(start+1,n+1):
                source[n] = j
                route.append(source[:])
            for j in range(1,dest+1):
                source[n] = j
                route.append(source[:])
        else:
            for j in range(start-1,dest-1,-1):
                source[n] = j
                route.append(source[:])
    else:
        clockwise = dest - start
        anticlock = n-dest + start
        if clockwise<anticlock:
            for j in range(start+1,dest+1):
                source[n] = j
                route.append(source[:])
        else:
            for j in range(start-1,0,-1):
                source[n] = j
                route.append(source[:])
            for j in range(n,dest-1,-1):
                source[n] = j
                route.append(source[:])
    return route

# following code used for testing

# route = hypercube_routing(5,[0,1,0,1,1],[1,1,0,0,0])
# print(route)
# route = karyncube_routing(2,4,[0,2],[3,3])
# print(route)
# route = cubeconncycle_routing(4,[0,1,0,1,3],[1,0,0,0,1])
# print(route)

# from random import choices,sample

# def random_hypercube(n):
#     nodes = [[0],[1]]
#     for i in range(1,n):
#         nodes0 = [ls+[0] for ls in nodes]
#         nodes1 = [ls+[1] for ls in nodes]
#         nodes = nodes0 + nodes1
#     targets = choices(nodes,k=len(nodes))
#     for i in range(len(nodes)):
#         #print(nodes[i],targets[i])
#         route = hypercube_routing(n,nodes[i],targets[i])
#         #print(route)
#     return

# #random_hypercube(25)

# def all_hypercube(n):
#     nodes = [[0],[1]]
#     for i in range(1,n):
#         nodes0 = [ls+[0] for ls in nodes]
#         nodes1 = [ls+[1] for ls in nodes]
#         nodes = nodes0 + nodes1
#     for i in range(len(nodes)):
#         for j in range(len(nodes)):
#             #print(nodes[i],nodes[j])
#             copy1 = nodes[i][:]
#             copy2 = nodes[j][:]
#             route = hypercube_routing(n,copy1,copy2)
#             #print(route)
#     return

# #all_hypercube(10)
# import math

# def perm_hypercube(n):
#     nodes = [[0],[1]]
#     for i in range(1,n):
#         nodes0 = [ls+[0] for ls in nodes]
#         nodes1 = [ls+[1] for ls in nodes]
#         nodes = nodes0 + nodes1
#     targets = []
#     if n%2 == 0:
#         num = int(n/2)
#         for i in range(len(nodes)):
#             targets.append(nodes[i][num:]+nodes[i][:num])
#     else:
#         num  = math.floor(n/2)
#         for i in range(len(nodes)):
#             targets.append(nodes[i][num+1:]+[nodes[i][num]]+nodes[i][:num])
#     for i in range(len(nodes)):
#         route = hypercube_routing(n,nodes[i],targets[i])
#     return

# #perm_hypercube(5)

# def random_karyncube(n,k):
#     original = [[i] for i in range(k)]
#     nodes = original[:]
#     for i in range(1,n):
#         new_nodes = []
#         for j in original:   
#             temp = [ls+[j[0]] for ls in nodes]
#             new_nodes.extend(temp)
#         nodes = new_nodes
#     targets = choices(nodes,k=len(nodes))
#     for i in range(len(nodes)):
#         print(nodes[i],targets[i])
#         route = karyncube_routing(n,k,nodes[i],targets[i])
#         print(route)
#     return

# #random_karyncube(2,6)

# def all_karyncube(n,k):
#     original = [[i] for i in range(k)]
#     nodes = original[:]
#     for i in range(1,n):
#         new_nodes = []
#         for j in original:   
#             temp = [ls+[j[0]] for ls in nodes]
#             new_nodes.extend(temp)
#         nodes = new_nodes
#     for i in range(len(nodes)):
#         for j in range(len(nodes)):
#             print(nodes[i],nodes[j])
#             copy1 = nodes[i][:]
#             copy2 = nodes[j][:]
#             route = karyncube_routing(n,k,copy1,copy2)
#             print(route)
#     return

# #all_karyncube(3,3)

# def random_cubeconncycle(n):
#     nodes = [[0],[1]]
#     for i in range(1,n):
#         nodes0 = [ls+[0] for ls in nodes]
#         nodes1 = [ls+[1] for ls in nodes]
#         nodes = nodes0 + nodes1
#     new_nodes = []
#     for i in range(len(nodes)):
#         for j in range(n):
#             new_nodes.append(nodes[i]+[j])
#     nodes = new_nodes
#     targets = choices(nodes,k=len(nodes))
#     for i in range(len(nodes)):
#         print(nodes[i],targets[i])
#         route = cubeconncycle_routing(n,nodes[i],targets[i])
#         print(route)
#     return

# random_cubeconncycle(4)

# def all_cubeconncycle(n):
#     nodes = [[0],[1]]
#     for i in range(1,n):
#         nodes0 = [ls+[0] for ls in nodes]
#         nodes1 = [ls+[1] for ls in nodes]
#         nodes = nodes0 + nodes1
#     new_nodes = []
#     for i in range(len(nodes)):
#         for j in range(n):
#             new_nodes.append(nodes[i]+[j])
#     nodes = new_nodes
#     targets = choices(nodes,k=len(nodes))
#     for i in range(len(nodes)):
#         for j in range(len(nodes)):
#             print(nodes[i],nodes[j])
#             copy1 = nodes[i][:]
#             copy2 = nodes[j][:]
#             route = cubeconncycle_routing(n,copy1,copy2)
#             print(route)
#     return

# #all_cubeconncycle(3)

