import pytest 
from pathlib import Path
from algorithms.djikstra import build_graph_from_routes, shortest_path


@pytest.fixture
def routes_path():
    return Path(__file__).resolve().parents[1] / "src" / "data" / "routes.json"


def test_distance(routes_path):
    graph = build_graph_from_routes(routes_path)
    distance, path = shortest_path(graph, "Central", "Parque")

    assert distance == 2.8
    assert path == ["Central", "Parque"]
