from Graph import Graph
from Food_Item import FoodItem
from copy import deepcopy
from calculation_tester import get_total_cost

def solve(graph : Graph, node : FoodItem) -> None:
    print(graph.current_path)
    if(len(graph.remaining_food) == 0):
        graph.update_optimal()
        return
    graph.remaining_food.remove(node.food_id)
    graph.current_path.path_list.append(node)
    for food in graph.remaining_food:
        #print(graph.current_path)
        #print("AAA")
        #print(graph.current_path.all_food_nodes[food])
        print(graph.remaining_food)
        cost = get_total_cost(node, graph.all_food_nodes[food])
        if(graph.current_path.net_energy_gain >= cost):
            graph.current_path.net_energy_gain -= cost
            solve(graph, graph.all_food_nodes[food])
            graph.current_path.net_energy_gain += cost
            graph.current_path.path_list.remove(graph.all_food_nodes[food])
            graph.remaining_food.append(graph.all_food_nodes[food].food_id)
    
def main():
    graph = Graph()
    graph.read_csv_data("./random_coordinates_energy.csv")
    graph.initialize_remaining_food()
    graph.current_path.net_energy_gain = graph.all_food_nodes[0].energy
    starting_node = graph.all_food_nodes[0]
    solve(graph, starting_node)
    print(graph.optimal_path)

if __name__ == "__main__":
    main()



