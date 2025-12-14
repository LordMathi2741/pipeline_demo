
from pathlib import Path
from algorithms.djikstra import shortest_path, build_graph_from_routes

if "main" in __name__:
    path = Path("src/data/routes.json")
    graph = build_graph_from_routes(path)
    start = input("Enter start location: ")
    end = input("Enter end location: ")
    distance, route = shortest_path(graph, start, end)
    if distance == float("inf"):
        print(f"No path found from {start} to {end}.")
    else:
        print(f"Shortest distance from {start} to {end} is {distance} km.")
        print("Route:", " -> ".join(route))
