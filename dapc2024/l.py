from collections import defaultdict
import sys

def main():
    rl = sys.stdin.readline
    n, m, t_change = map(int, rl().split())
    roads = [tuple(map(int, rl().split())) for _ in range(m)]

    # 1. Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for x, y, L, v1, v2 in roads:
        adj[x].append((y, L, v1, v2))
        adj[y].append((x, L, v1, v2))

    # 2.Explore promising edges first: optimistic time L / max(v1, v2)
    for u in range(1, n + 1):
        adj[u].sort(key=lambda e: e[1] / (e[2] if e[2] > e[3] else e[3]))

    # 3. Use DFS to find all paths from 1 to n without cycle
    t_min = [float("INF")] # boxed to avoid nonlocal
    visit = set([1])

    def _edge_time(length, v1, v2, t_total):
        if t_total >= t_change:  # Use v2
            t_road = length / v2
        else:
            t_slow = length / v1
            if t_total + t_slow <= t_change:  # Use v1
                t_road = t_slow
            else:  # Use v1 and v2
                t_slow = t_change - t_total
                l_slow = t_slow * v1
                l_fast = length - l_slow
                t_fast = l_fast / v2
                t_road = t_slow + t_fast
        return t_road

    def _dfs(node, t_total):
        if node == n:
            t_min[0] = min(t_min[0], t_total) # change variable outside of the function
            return

        for nei, length, v1, v2 in adj[node]:
            if nei in visit:
                continue

            # Compute time on this road
            t_road = _edge_time(length, v1, v2, t_total)
            if t_total + t_road >= t_min[0]:
                continue

            visit.add(nei)
            _dfs(nei, t_total+t_road)
            visit.discard(nei)

    _dfs(1, 0)
    print(t_min[0])


if __name__ == "__main__":
    main()