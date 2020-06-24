# uses python3

import sys

def getData():
    # lines = sys.stdin.read().splitlines()
    # [k, t] = [int(i) for i in lines[0].split()]
    # r = lines[1:]
    # return k, t, r
    # The code below is for temporary use.
    [k, t] = [int(i) for i in input().split()]
    r = []
    while True:
        read = input()
        if read != "":
            r.append(read)
        else:
            break
    return k, t, r


def getDBGraph(k, rs):
    lenRead = len(rs[0])

    # dictIndToValue : Mapping from indexVertex to valueVertex
    # dictValueToInd : Mapping from valueVertex to indexVertex
    dictIndToValue = {}  # Initialize
    dictValueToInd = {}
    # gr :  De Bruijn Graph
    # degrees :  [inDegree, outDegree] for each Vertex
    gr = []
    degr = []
    counter = 0
    for i in range(len(rs)):
        for j in range(lenRead - (k - 1)):
            prefix = rs[i][j:j + (k - 1)]
            suffix = rs[i][j + 1: j + 1 + (k - 1)]

            if prefix not in dictValueToInd:
                dictValueToInd[prefix] = counter
                dictIndToValue[counter] = prefix
                gr.append([])
                degr.append([0, 0])
                counter += 1
            if suffix not in dictValueToInd:
                dictValueToInd[suffix] = counter
                dictIndToValue[counter] = suffix
                gr.append([])
                degr.append([0, 0])
                counter += 1
            if dictValueToInd[suffix] not in gr[dictValueToInd[prefix]]:
                gr[dictValueToInd[prefix]].append(dictValueToInd[suffix])
                degr[dictValueToInd[prefix]][0] += 1
                degr[dictValueToInd[suffix]][1] += 1
    return gr, degr

# Greg G.
# Find all nodes with outdegree > 1, except self loops (OUT nodes) and indegree > 1, except self loops (IN nodes). We're looking for paths that start with an OUT node and end with an IN node.
# From each of these OUT nodes, do DFS that lists all possible paths of less than t edges. (Skip self-loops!) Don't stop at the first IN node, go until you have t edges.
# Discard paths having no IN nodes (not counting the start node).
# For each starting OUT node, compare all paths starting there with each other (yes, O(n^2)). Find first matching IN node in both paths. Check if the two paths are indeed disjoint between the start node and the first matching IN node.
# Check if you haven't already stored the same bubble! This can happen because the paths end at length t so you may have several paths with the same intermediary nodes.
# Increase bubble count if the above is all true.

# Yuanfei
# 1. Break raw reads to k-mers and construct the de-Bruijn graph.
# 2a.Collect all vertices in the graph with out degree > 1 in an ArrayList (I called it validOut).
# 2b.Collect all vertices in the graph with in degree > 1 in a HashSet (I called it validIn).
# 3. For each vertex v in validOut, use v as root and construct a traversal tree using DFS on the de-Bruijn graph. be careful not to allow overlapping traversal paths or paths whose length is bigger than the threshold;
# 4. Traverse the tree constructed in step 3 and record the path from the root to current node if current node is contained in validIn HashSet. I used this data structure to store all possible paths from root to any possible end nodes in validIn: Hashtable<Integer, ArrayList<ArrayList<Integer>>>;
# 5. for each possible pair of paths between (u, v) check if the two paths are disjoint, if true increase totalBubbleCount by 1.

# Jose Pablo Escobedo
# 1.From every node with out degree > 1 (Skip self-loops!), perform a BFS with paths lengths <= t (careful, paths lengths are measured in number of edges here).
#   Save all the bubble candidates: the origin is the node with degree > 1, and the targets are all the "visited more than once" nodes in
#   their respective BFS. Just avoid overlapping paths (cycles).
# 2.For every pair of candidates of step 1, perform a DFS to find all paths from origin to target (also of length t --on the edges).
# 3.For all pairs of paths from origins to their respective targets, compute the number of bubbles by counting disjoint paths.

# Find all Paths starting from u. Skip self-loops!
# Each Path must have up to t levels of edge.
# Save the paths with t-th edge ending in vertex with more than one in-degree + selfLoops



def getBubbles(gr, degs, t):
    def getPaths(u, t) :    # def BFS(self, s):
            candidates = []
            visited = [False] * (len(gr))   # Mark all the vertices as not visited
            queue = [u] # Create a queue for BFS
            visited[u] = True   # Mark the source node as visited and enqueue it
            level = 0
            while queue and countThreshold <= t:
                s = queue.pop(u)    # Dequeue a vertex from queue and print it
                # pathprint(s, end=" ")

                # Get all adjacent vertices of the dequeued vertex s.
                # If a adjacent has not been visited, then mark it visited and enqueue it
                for i in gr[s]:
                    if visited[i] == False:
                        queue.append(i)
                        visited[i] = True
                        level += 1
                    else :
                        candidates.append(i)

    # For each Vertex with out-degree > 1 + selfLoops, get all Paths
    for u in range(len(gr)):
        selfLoops = gr[u].count(u)
        if degs[u[1] <= 1 + selfLoops: continue
        paths = getPahs(u, t)


if __name__ == "__main__":
    k, t, reads = getData()
    lengthOfRead = len(reads[0])
    graph, degrees = getDBGraph(k, reads)
    getBubbles(graph, degrees, t)