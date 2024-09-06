{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "c919798d-45b3-4618-97af-0b42230fe0c8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "y is am even number\n"
     ]
    }
   ],
   "source": [
    "x = -5\n",
    "y = -10\n",
    "if x%2 == 0:\n",
    "  print(\"x is am odd number\")\n",
    "else:\n",
    "  print(\"y is am even number\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "77d11f99-c7c8-435d-a81f-a251cb246e47",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Shortest path from A to D: A -> B -> C -> D\n",
      "Total distance: 4\n"
     ]
    }
   ],
   "source": [
    "import heapq\n",
    "\n",
    "class Graph:\n",
    "    def __init__(self):\n",
    "        self.vertices = {}\n",
    "\n",
    "    def add_vertex(self, vertex):\n",
    "        if vertex not in self.vertices:\n",
    "            self.vertices[vertex] = []\n",
    "\n",
    "    def add_edge(self, from_vertex, to_vertex, weight):\n",
    "        self.add_vertex(from_vertex)\n",
    "        self.add_vertex(to_vertex)\n",
    "        self.vertices[from_vertex].append((to_vertex, weight))\n",
    "        self.vertices[to_vertex].append((from_vertex, weight))\n",
    "\n",
    "    def dijkstra(self, start_vertex):\n",
    "        # Priority queue to keep track of the next vertex to explore\n",
    "        priority_queue = [(0, start_vertex)]\n",
    "        # Dictionary to store the shortest path to each vertex\n",
    "        shortest_paths = {vertex: float('inf') for vertex in self.vertices}\n",
    "        shortest_paths[start_vertex] = 0\n",
    "        # Dictionary to store the actual shortest path (vertex sequence)\n",
    "        previous_vertices = {vertex: None for vertex in self.vertices}\n",
    "\n",
    "        while priority_queue:\n",
    "            current_distance, current_vertex = heapq.heappop(priority_queue)\n",
    "\n",
    "            # If the distance of the current vertex is already optimal, skip\n",
    "            if current_distance > shortest_paths[current_vertex]:\n",
    "                continue\n",
    "\n",
    "            for neighbor, weight in self.vertices[current_vertex]:\n",
    "                distance = current_distance + weight\n",
    "\n",
    "                # Only consider this new path if it's shorter\n",
    "                if distance < shortest_paths[neighbor]:\n",
    "                    shortest_paths[neighbor] = distance\n",
    "                    previous_vertices[neighbor] = current_vertex\n",
    "                    heapq.heappush(priority_queue, (distance, neighbor))\n",
    "\n",
    "        return shortest_paths, previous_vertices\n",
    "\n",
    "    def print_shortest_path(self, start_vertex, end_vertex):\n",
    "        # Reconstruct the shortest path from start to end vertex\n",
    "        shortest_paths, previous_vertices = self.dijkstra(start_vertex)\n",
    "        path = []\n",
    "        current_vertex = end_vertex\n",
    "\n",
    "        while current_vertex is not None:\n",
    "            path.append(current_vertex)\n",
    "            current_vertex = previous_vertices[current_vertex]\n",
    "\n",
    "        path = path[::-1]\n",
    "\n",
    "        if shortest_paths[end_vertex] == float('inf'):\n",
    "            print(f\"No path from {start_vertex} to {end_vertex}.\")\n",
    "        else:\n",
    "            print(f\"Shortest path from {start_vertex} to {end_vertex}: {' -> '.join(path)}\")\n",
    "            print(f\"Total distance: {shortest_paths[end_vertex]}\")\n",
    "\n",
    "# Example usage\n",
    "graph = Graph()\n",
    "graph.add_edge('A', 'B', 1)\n",
    "graph.add_edge('A', 'C', 4)\n",
    "graph.add_edge('B', 'C', 2)\n",
    "graph.add_edge('B', 'D', 5)\n",
    "graph.add_edge('C', 'D', 1)\n",
    "\n",
    "graph.print_shortest_path('A', 'D')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cd913dc9-b4df-4c32-b8c8-a6ea8b6eb096",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
