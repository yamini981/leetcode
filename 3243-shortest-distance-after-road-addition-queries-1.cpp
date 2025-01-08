class Solution {
public:

    int bfs(int start, int end, int n, vector<vector<int>>& adjList) {
            vector<int> dist(n, INT_MAX);
            queue<int> q;
            dist[start] = 0;
            q.push(start);

            while (!q.empty()) {
                int curr = q.front();
                q.pop();

                for (int u : adjList[curr]) {
                    if (dist[u] > dist[curr] + 1) {
                        dist[u] = dist[curr] + 1;
                        q.push(u);
                    }
                }
            }

        return dist[end];
        }
    vector<int> shortestDistanceAfterQueries(int n, vector<vector<int>>& queries) {
        
        vector<vector<int>> adjacencyList(n);
        vector<int> ret(queries.size());
        for (int i = 0; i < n - 1; i ++) {
            adjacencyList[i].push_back(i + 1);
        }

        for (int i = 0; i < queries.size(); i++) {
            adjacencyList[queries[i][0]].push_back(queries[i][1]);
            ret[i] = bfs(0, n - 1, n, adjacencyList);
        }


        
        return ret;
    }
};