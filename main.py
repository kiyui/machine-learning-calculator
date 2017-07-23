from sklearn import tree

# Generators are the best
def generate_data(a, b, operator, calculate_result):
    for i in range(a, b):
        for ii in range(a, b):
            yield [i, operator, ii], calculate_result(i, ii)
            yield [ii, operator, i], calculate_result(ii, i)

# We are addicted to C
def main(i, ii):
    clf = tree.DecisionTreeRegressor()

    # Special mapping
    operators = {
        '+': 0,
        '-': 1,
        '*': 2,
        '/': 3,
    }

    # Create generators
    add_data = generate_data(i, ii, operators['+'], lambda a, b: a + b)
    minus_data = generate_data(i, ii, operators['-'], lambda a, b: a - b)
    times_data = generate_data(i, ii, operators['*'], lambda a, b: a * b)
    divide_data = generate_data(i, ii, operators['/'], lambda a, b: a / b)

    # Generate dataset
    all_data = [i for i in add_data] + [i for i in minus_data] + [i for i in times_data] + [i for i in divide_data]

    # We use map because functional programming is the best programming
    x = list(map(lambda l: l[0], all_data))
    y = list(map(lambda l: l[1], all_data))

    # Training our model with the best mathematical data
    clf = clf.fit(x, y)

    print('Input format is float operator float, for example: 3 * 8')
    while True:
        try:
            a, o, b = input('Calculate: ').split()
            result = clf.predict([[float(a), operators[o], float(b)]])
            print("Result of operation %s %s %s is %f" % (a, o, b, result))
        except (EOFError, KeyboardInterrupt):
            return False

# Good code always has this because it is the best code
if __name__ == '__main__':
    try:
        a, b = input('Please input training range (ex. 1 100) : ').split()
        main(int(a), int(b))
    except (EOFError, KeyboardInterrupt):
        print('Goodbisexual')
