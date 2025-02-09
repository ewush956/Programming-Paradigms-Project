from Graph import Graph
from Food_Item import FoodItem
from copy import deepcopy
from calculation_tester import get_total_cost

def solve(graph : Graph, node : FoodItem) -> None:
    if(len(graph.remaining_food) == 0):
        graph.update_optimal()
        return
    graph.remaining_food.remove(node)
    graph.current_path.path_list.append(node)
    for food in range(0, len(graph.remaining_food)):
        cost = get_total_cost(node, graph.remaining_food[food])
        if(graph.current_path.net_energy_gain >= cost):
            graph.current_path.net_energy_gain -= cost
            solve(graph, graph.remaining_food[food])
            graph.current_path.path_list.remove(graph.remaining_food[food])
            graph.current_path.net_energy_gain += cost
            graph.remaining_food.append(graph.remaining_food[food])
    
def main():
    graph = Graph()
    graph.read_csv_data("./random_coordinates_energy.csv")
    graph.initialize_remaining_food()
    graph.current_path.net_energy_gain = graph.remaining_food[0].energy
    starting_node = graph.all_food_nodes[0]
    solve(graph, starting_node)
    print(graph.optimal_path)

if __name__ == "__main__":
    main()



