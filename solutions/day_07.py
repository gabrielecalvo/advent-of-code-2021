from utils import get_input, test_func


# +
def process_input(data):
    return tuple([int(i) for i in data.split(",")])

test_content = process_input(get_input("day07_test.txt"))
content = process_input(get_input("day07.txt"))


# -

# ## Day 7

def calculate_linear_cost(xs, target):
    return sum([abs(x-target) for x in xs])


def brute_force(xs, cost_func):
    min_edge = min(xs)
    max_edge = max(xs)
    result = cost_func(xs, max_edge)

    for i in range(min_edge, max_edge):
        new = cost_func(xs, i)
        if new < result:
            result = new
    return result


def search_minimum(xs, cost_func, verbose=False):
    top = max(xs)
    bottom = min(xs)
    step = (top-bottom) / 4
    direction = 1
    
    prev_target = int(sum(xs)/len(xs))
    next_target = int(prev_target + step*direction)
    
    iteration = 0
    while True:
        cost_prev = cost_func(xs, prev_target)
        cost_next = cost_func(xs, next_target)
        if step < 1: break
        
        if verbose: print(f"{prev_target=} ({cost_prev=}), {next_target=} ({cost_next=})")
        
        if cost_prev < cost_next:
            step *= 0.5
            direction *= -1
        else:
            step *= 0.7
            prev_target = next_target
        next_target = int(prev_target + step*direction)

        if verbose: print(f"{direction=} ({step=}), {next_target=}")
        iteration += 1 
        if iteration > 15:
            raise ValueError
    
    return min(cost_prev, cost_next)


# ## part 1

test_func(37, brute_force, xs=test_content, cost_func=calculate_linear_cost)
test_func(343441, brute_force, xs=content, cost_func=calculate_linear_cost)

test_func(37, search_minimum, xs=test_content, cost_func=calculate_linear_cost)
test_func(343441, search_minimum, xs=content, cost_func=calculate_linear_cost)


# ## part 2

# +
def _move_cost(delta):
    return sum([i for i in range(delta+1)])
    
def calculate_exp_cost(xs, target):
    return sum([_move_cost(abs(x-target)) for x in xs])


# -

test_func(168, search_minimum, xs=test_content, cost_func=calculate_exp_cost)
test_func(98925151, search_minimum, xs=content, cost_func=calculate_exp_cost)


