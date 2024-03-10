from road_network import UnifiedRoadNetwork

def main():
    network = UnifiedRoadNetwork()

    # Assuming the UnifiedRoadNetwork.add_connection method has been defined to add connections.
    # Here you add your connections based on actual distances.
    network.add_connection('VA', 'BU', 10)  # Vancouver to Burnaby
    network.add_connection('BU', 'RI', 15)  # Burnaby to Richmond
    network.add_connection('RI', 'SU', 20)  # Richmond to Surrey
    # Add more connections to reflect the realistic connectivity map

    print("Unified Road Network Pathfinding")
    print("Available cities: VA (Vancouver), BU (Burnaby), RI (Richmond), SU (Surrey), etc.")

    print("**************************************************")
    # Input from the user
    start_city = input("Enter start city code: ").upper()
    goal_city = input("Enter goal city code: ").upper()
    algorithm_choice = input("Choose the algorithm (A*, Dijkstra, Grassfire): ")
    
    # Pathfinding based on user choice
    if algorithm_choice.lower() == "a*":
        path = network.a_star_search(start_city, goal_city)
    elif algorithm_choice.lower() == "dijkstra":
        path = network.dijkstra_search(start_city, goal_city)
    elif algorithm_choice.lower() == "grassfire":
        path = network.grassfire_search(start_city, goal_city)
    else:
        print("Invalid algorithm choice.")
        return
    
    # Output the path
    if path:
        print(f"Path found: {' -> '.join(path)}")
    else:
        print("No path found between the specified cities.")

if __name__ == "__main__":
    main()
