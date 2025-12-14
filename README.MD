# Project of Routes

This project aims to practice skills in generating continuous integration (CI) pipelines using GitHub Actions. It implements a system to calculate the shortest path between different stops.

## Project Structure

```
.
├── .gitignore
├── [`pyproject.toml`](pyproject.toml )
├── [`README.md`](README.md )
├── [`requirements.txt`](requirements.txt )
├── .github/
│   └── workflows/
│       └── [`.github/workflows/pipeline.yml`](.github/workflows/pipeline.yml )
├── .pytest_cache/
│   └── ...
└── src/
    ├── [`src/app.py`](src/app.py )
    ├── algorithms/
    │   └── [`src/algorithms/djikstra.py`](src/algorithms/djikstra.py )
    └── data/
        └── [`src/data/routes.json`](src/data/routes.json )
    └── tests/
        └── [`src/tests/test.py`](src/tests/test.py )
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/LordMathi2741/pipeline_demo.git
   cd pipeline_demo
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the application, use the following command:

```bash
python [`src/app.py`](src/app.py )
```

You will be prompted to enter the starting location and the destination.

## Tests

Tests are implemented using `pytest`. To run the tests, use the following command:

```bash
pytest [`src/tests/test.py`](src/tests/test.py )
```

## CI/CD

This project includes a CI pipeline configured in [pipeline.yml](.github/workflows/pipeline.yml) that runs on every push or pull request to the `main` branch.

## Contributions

Contributions are welcome. If you would like to contribute, please open an issue or a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
