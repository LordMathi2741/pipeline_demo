from pathlib import Path
from algorithms.djikstra import build_graph_from_routes, shortest_path


def test_distance():
    path = Path("src/data/routes.json")
    graph = build_graph_from_routes(path)
    start, end = "Central", "Parque"
    distance, path = shortest_path(graph, start, end)
    assert distance == 2.8
    assert path == ["Central", "Parque"]