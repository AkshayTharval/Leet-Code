from collections import defaultdict
class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        graph = defaultdict(list)
        for v in connections:
            graph[v[0]].append(v[1])
            graph[v[1]].append(v[0])

        visited = [None for i in range(n)]
        lowest = [None for i in range(n)]

        cur = 0
        start = 0
        res = []
        self.cur = 0

        def dfs(node, parent):
            if visited[node] is None:
                visited[node] = self.cur
                lowest[node] = self.cur
                self.cur += 1
                for n in graph[node]:
                    if visited[n] is None:
                        dfs(n, node)

                if parent is not None:
                    l = min([lowest[i] for i in graph[node] if i != parent] + [lowest[node]])
                else:
                    l = min(lowest[i] for i in graph[node] + [lowest[node]])
                lowest[node] = l

        dfs(0, None)

        for v in connections:
            if lowest[v[0]] > visited[v[1]] or lowest[v[1]] > visited[v[0]]:
                res.append(v)
        return res