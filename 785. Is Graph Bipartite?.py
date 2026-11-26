class Solution(object):

    def dfs(self, current_node, visited, graph, color):

        visited[current_node] = color

        for adjNode in graph[current_node]:

            if visited[adjNode] == color:
                return False

            elif visited[adjNode] == -1:

                ans = self.dfs(adjNode, visited, graph, 1-color)

                if ans == False:
                    return False

        return True

    def isBipartite(self, graph):

        total_node = len(graph)

        visited = [-1] * total_node

        for index in range(total_node):

            if visited[index] == -1:

                ans = self.dfs(index, visited, graph, 0)

                if ans == False:
                    return False

        return True
