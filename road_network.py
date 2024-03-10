from collections import deque
import heapq

# Example heuristic matrix with direct distances from Google Maps (simplified)
heuristic_matrix = {
    # Placeholder distances - replace these with actual data
    'VA': {'LA': 45, 'RI': 20, 'BU': 10, 'SU': 30},
    'BU': {'LA': 35, 'RI': 15, 'VA': 10, 'SU': 25},
    'RI': {'LA': 30, 'BU': 15, 'VA': 20, 'SU': 20},
    'SU': {'LA': 25, 'BU': 25, 'VA': 30, 'RI': 20},
    # Add all other cities and their heuristic distances
}

def heuristic(city1, city2):
    """Return the heuristic distance between two cities."""
    return heuristic_matrix.get(city1, {}).get(city2, float('inf'))

class UnifiedRoadNetwork:
    def __init__(self):
        self.network = {}
    
    def add_connection(self, city1, city2, distance):
        """Add a bidirectional road connection between two cities with the given distance."""
        if city1 not in self.network:
            self.network[city1] = {}
        if city2 not in self.network:
            self.network[city2] = {}
        self.network[city1][city2] = distance
        self.network[city2][city1] = distance
    
    def neighbors(self, city):
        """Return neighboring cities and distances for a given city."""
        return self.network.get(city, {})
    
    def a_star_search(self, start, goal):
        """Perform A* search to find the shortest path between start and goal cities."""
        open_set = [(0 + heuristic(start, goal), 0, start, [start])]
        heapq.heapify(open_set)
        visited = set()

        while open_set:
            _, current_cost, current_city, path = heapq.heappop(open_set)
            if current_city == goal:
                return path
            if current_city not in visited:
                visited.add(current_city)
                for neighbor, distance in self.neighbors(current_city).items():
                    if neighbor not in visited:
                        total_cost = current_cost + distance
                        heapq.heappush(open_set, (total_cost + heuristic(neighbor, goal), total_cost, neighbor, path + [neighbor]))
        return []
    
    # Dijkstra's Search
    def dijkstra_search(self, start, goal):
        open_set = [(0, start, [])]
        heapq.heapify(open_set)
        visited = set()

        while open_set:
            cost, current, path = heapq.heappop(open_set)
            if current == goal:
                return path + [current]
            if current not in visited:
                visited.add(current)
                for neighbor, distance in self.neighbors(current).items():
                    heapq.heappush(open_set, (cost + distance, neighbor, path + [current]))

        return []

    # Grassfire Search (BFS Simulation)
    def grassfire_search(self, start, goal):
        queue = deque([(start, [start])])
        visited = set()

        while queue:
            current, path = queue.popleft()
            if current == goal:
                return path
            if current not in visited:
                visited.add(current)
                for neighbor in self.neighbors(current):
                    queue.append((neighbor, path + [neighbor]))

        return []

    def display_network(self):
        """Prints the road network for visualization."""
        for city, connections in self.network.items():
            print(f"{city}: {connections}")