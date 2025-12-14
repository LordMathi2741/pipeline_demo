from __future__ import annotations
import heapq
import json
from pathlib import Path
from typing import Dict, Tuple


def build_graph_from_routes(routes_path: Path) -> Dict[str, Dict[str, float]]:
    """Load routes.json and build an undirected weighted graph using stops.

    Each route defines a chain: origin -> stops... -> destination. The weight
    between consecutive nodes is the route distance divided evenly by the
    number of hops in that chain. This keeps edges proportional to the total
    distance when only aggregate length is provided.
    """

    with routes_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    graph: Dict[str, Dict[str, float]] = {}

    for route in data.get("routes", []):
        chain = [route["origin"], *route.get("stops", []), route["destination"]]
        if len(chain) < 2:
            continue

        hops = len(chain) - 1
        weight = route.get("distance_km", 1.0) / hops if hops else 1.0

        for a, b in zip(chain, chain[1:]):
            graph.setdefault(a, {})[b] = min(graph.get(a, {}).get(b, float("inf")), weight)
            graph.setdefault(b, {})[a] = min(graph.get(b, {}).get(a, float("inf")), weight)

    return graph


def djikstra(graph: Dict[str, Dict[str, float]], start: str) -> Tuple[Dict[str, float], Dict[str, str | None]]:
    
    distances: Dict[str, float] = {node: float("inf") for node in graph}
    previous: Dict[str, str | None] = {node: None for node in graph}

    if start not in graph:
        return distances, previous

    distances[start] = 0.0
    queue = [(0.0, start)]

    while queue:
        current_distance, current = heapq.heappop(queue)
        if current_distance > distances[current]:
            continue

        for neighbor, weight in graph[current].items():
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current
                heapq.heappush(queue, (new_distance, neighbor))

    return distances, previous


def shortest_path(graph: Dict[str, Dict[str, float]], start: str, end: str) -> Tuple[float, list[str]]:
    """Return total distance and node list for the shortest path start->end."""

    distances, previous = djikstra(graph, start)
    if distances.get(end, float("inf")) == float("inf"):
        return float("inf"), []

    path = []
    node: str | None = end
    while node is not None:
        path.append(node)
        node = previous[node]
    path.reverse()
    return distances[end], path