# Driverless-Car-Pathfinding in the Greater Vancouver Area

This project implements three classic pathfinding algorithms (A*, Dijkstra, and Grassfire) within a simulated road network of the Greater Vancouver area. The goal is to guide a driverless car from one city hall to another, utilizing an offline map for navigation. This README provides an overview of the project structure, setup instructions, and usage details.

## Project Structure

The project consists of two main Python files:

- `road_network.py`: Defines the `UnifiedRoadNetwork` class, which encapsulates the road network and includes methods for adding connections between cities and performing pathfinding using A*, Dijkstra, and Grassfire algorithms.
- `network_usage.py`: A user interface script that interacts with the `UnifiedRoadNetwork` class. It allows users to input start and goal cities and select a pathfinding algorithm to find the optimal path.

## Setup Instructions

1. **Clone the Repository**: Clone this project to your local machine using Git.

    ```bash
    git clone [URL_of_the_GitHub_repository]
    ```

2. **Install Python**: Ensure you have Python 3.6 or later installed on your system. You can download Python from [the official website](https://www.python.org/downloads/).

3. **Run the Program**: Navigate to the project directory and run `network_usage.py` to start the pathfinding application.

    ```bash
    cd Driverless-Car-Pathfinding
    python network_usage.py
    ```

## Usage

When you run `network_usage.py`, the script will prompt you for the following inputs:

- **Start City Code**: Enter the two-letter abbreviation of the start city (e.g., `VA` for Vancouver).
- **Goal City Code**: Enter the two-letter abbreviation of the destination city (e.g., `LA` for Langley).
- **Algorithm**: Choose the pathfinding algorithm by typing `A*`, `Dijkstra`, or `Grassfire`.

After receiving the inputs, the program will display the optimal path found by the selected algorithm.

## Customizing the Road Network

The `road_network.py` script can be modified to reflect actual distances and connections between cities in the Greater Vancouver area. To add a new city connection, use the `add_connection` method of the `UnifiedRoadNetwork` class:

```python
network.add_connection('City1_Code', 'City2_Code', distance_in_km)
