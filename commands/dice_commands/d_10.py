from random import randint

results_of_d10s = []
summed_d10s = []

# => Pushes the value of the dice to the list
def push(value, first_arr, second_arr):
    first_arr.append(f"{value}")
    second_arr.append(value)

def d_10():
    definer = randint(1, 3)
    selector = randint(1, 4)
    # -> Weak rolls :(
    if definer == 1:
        # => Weakest roll
        if selector == 1 or 2:
            d10 = randint(1, 4)
            push(d10, results_of_d10s, summed_d10s)
        
        # => Weak roll
        if selector == 3:
            d10 = randint(2, 5)
            push(d10, results_of_d10s, summed_d10s)

        # => Raw roll
        if selector == 4:
            d10 = randint(1, 10)
            push(d10, results_of_d10s, summed_d10s)
    #====================================#
    # -> Medium rolls :|
    elif definer == 2:
        if selector == 1:
            d10 = randint(4, 1)
            push(d10, results_of_d10s, summed_d10s)
        if selector == 2 or 3:
            d10 = randint(5, 2)
            push(d10, results_of_d10s, summed_d10s)
        if selector == 4:
            d10 = randint(6, 3)
            push(d10, results_of_d10s, summed_d10s)
    #====================================#
    # -> Strong rolls :)
    elif definer == 3:
        if selector == 1:
            d10 = randint(7, 4)
            push(d10, results_of_d10s, summed_d10s)
        if selector == 2:
            d10 = randint(6, 5)
            push(d10, results_of_d10s, summed_d10s)
        if selector == 3:
            d10 = randint(5, 6)
            push(d10, results_of_d10s, summed_d10s)
        if selector == 4:
            d10 = randint(4, 7)
            push(d10, results_of_d10s, summed_d10s)
    #====================================#
    print(results_of_d10s)

# => Testing loop
def test():
    text_input = ''

    while text_input != '0':
        text_input = input('Insira um número!')
        d_10()
