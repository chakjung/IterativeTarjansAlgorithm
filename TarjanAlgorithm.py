from collections import defaultdict


class TarjanAlgorithm:
    def __init__(self, Edges):
        # Turn Edges to Nodes
        self.Nodes = defaultdict(list)
        for src, dst in Edges:
            self.Nodes[src].append(dst)
            self.Nodes.setdefault(dst, [])

        # Initially no SCC exists
        self.SCCCtr = 0
        self.SCCs = set()
        self.SCCIdx = [None]*(len(self.Nodes)+1)
        self.SCCLoLink = [None]*(len(self.Nodes)+1)

        # Declared at class level, to avoid repetitive (de)allocation
        self.OnSCCStack = [False]*(len(self.Nodes)+1)

    def getSCCs(self):
        for node in self.Nodes.keys():
            if self.SCCLoLink[node] is None:
                self.assignSCC(node)

        return self.SCCs

    def assignSCC(self, node):
        SCCStack = []

        # Declared at class level, to avoid repetitive (de)allocation
        # OnSCCStack = [False]*(len(self.Nodes)+1)

        # parent, exploring child, children iter
        DFSStack = [[node, None, iter(self.Nodes[node])]]

        while DFSStack:
            node, exploringChild, childrenIter = DFSStack[-1]

            if self.SCCIdx[node] is None:
                self.SCCIdx[node] = self.SCCCtr
                self.SCCLoLink[node] = self.SCCCtr
                self.SCCCtr += 1

                SCCStack.append(node)
                self.OnSCCStack[node] = True

            if exploringChild is not None:
                self.SCCLoLink[node] = min(self.SCCLoLink[node],
                                           self.SCCLoLink[exploringChild])

            for child in childrenIter:
                if self.SCCIdx[child] is None:
                    DFSStack[-1][1] = child
                    DFSStack.append([child, None, iter(self.Nodes[child])])
                    break

                if self.OnSCCStack[child]:
                    self.SCCLoLink[node] = min(self.SCCLoLink[node],
                                               self.SCCLoLink[child])

            # If child appended onto the DFSStack
            # Skip current iteration and run DFS on that child
            if DFSStack[-1][0] != node:
                continue

            if self.SCCLoLink[node] == self.SCCIdx[node]:  # SCC completed
                SCC = [node]
                self.OnSCCStack[node] = False
                while (SCCPeer := SCCStack.pop()) != node:
                    SCC.append(SCCPeer)
                    self.OnSCCStack[SCCPeer] = False

                self.SCCs.add(frozenset(SCC))

            DFSStack.pop()
