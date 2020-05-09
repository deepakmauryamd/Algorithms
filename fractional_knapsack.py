# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    total_value = 0.
    # write your code here
    value_by_weight = {}
    i = 0
    for value, weight in zip(values,weights):
        value_by_weight[i] = (value / weight)
        i += 1
    
    # sorting dictionary by value
    value_by_weight_sorted = {k: v for k, v in sorted(value_by_weight.items(), key=lambda item: item[1], reverse=True)}
   
    sorted_keys = list(value_by_weight_sorted.keys())
    
    j =0
    
    while(capacity > 0 and j < len(sorted_keys)):
        if(capacity >= weights[sorted_keys[j]]):
            total_value += values[sorted_keys[j]]
            capacity -= weights[sorted_keys[j]]
          
        else:
            total_value += capacity * value_by_weight[sorted_keys[j]]
            capacity = 0
            
        j += 1

    return total_value



if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
