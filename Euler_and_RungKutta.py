from matplotlib import pyplot


def my_function(t0, v0):
    return 9 - 0.2*v0 - 0.27 * (v0 ** 1.5)


def euler(t0, v0, tn, step):
    # Calculating step size
    h1 = (tn - t0) / step

    # print('\n-----------SOLUTION-----------')
    # print('------------------------------')
    # print('t0\t\tv0\t\tslope\t\tvn')
    # print('------------------------------')
    for i in range(step):  # i for iteration
        slope = my_function(t0, v0)
        vn = v0 + h1 * slope
        # print('%.4f\t%.4f\t%0.4f\t%.4f' % (t0, v0, slope, vn))
        # print('------------------------------')
        listOfV.append(v0)
        listOfT.append(t0)
        v0 = vn
        t0 = t0 + h1
    # print('\nAt x=%.4f, y=%.4f' % (tn, vn))
    print(f'Euler\'s with h = {h1}: v({tn}) = {vn}')


def improved_euler(t0, v0, tn, step):
    h = (tn - t0) / step
    # print('\n--------SOLUTION--------')
    # print('-------------------------')
    # print('xn\t\tvn\t\tvn+1')
    # print('-------------------------')
    for i in range(step): # i for iteration
        k1 = my_function(t0, v0)
        u = v0 + h * k1
        k2 = my_function(t0 + h, u)
        vn = v0 + (h / 2) * (k1 + k2)

        listOfT.append(t0)
        listOfV.append(v0)

        # print(f'v({t0}) = {vn}')

        v0 = vn
        t0 = t0 + h
    print(f'Improved Euler\'s method with h = {h}: v({tn}) = {vn}')

def runge_kutta(t0, v0, tn, step):
    # Calculating step size
    h = (tn - t0) / step

    # print('\n--------SOLUTION--------')
    # print('-------------------------')
    # print('xn\t\tvn\t\tvn+1')
    # print('-------------------------')
    for i in range(step):  # i for iteration
        k1 = h * my_function(t0, v0)
        k2 = h * my_function(t0 + h / 2, v0 + k1 / 2)
        k3 = h * my_function(t0 + h / 2, v0 + k2 / 2)
        k4 = h * my_function(t0 + h, v0 + k3)
        t = (k1 + 2 * k2 + 2 * k3 + k4) / 6
        vn = v0 + t
        # print('%.4f\t%.4f\t%.4f' % (t0, v0, vn))
        # print(f'-------------------------\t\tk1 = {k1}, k2 = {k2}, k3 = {k3}, k4 = {k4}, T = {t}')
        listOfT.append(t0)
        listOfV.append(v0)
        v0 = vn
        t0 = t0 + h

    # print('\nAt x=%.4f, y=%.4f' % (tn, vn))
    print(f'Runge Kutta with h = {h}: v({tn}) = {vn}')

# TODO: Euler's method.
listOfV = []
listOfT = []

print('Enter initial conditions:')
t0 = float(input('t0 = '))
v0 = float(input('v0 = '))

print('Enter the point you want to approximate: ')
tf = float(input('tf = '))

print('Enter number of steps:')
stepOne = int(input('Number of steps in the first approximation = '))
stepTwo = int(input('Number of steps in the second approximation: '))

# first step size
euler(t0, v0, tf, stepOne)
pyplot.plot(listOfT, listOfV, color='limegreen', marker='.', linewidth=1.5, label='Euler with h = 0.5')

# prepare to do again
listOfV = []
listOfT = []

# second step size
euler(t0, v0, tf, stepTwo)  # I'm reusing my two lists so I need to call euler() after plotting.
pyplot.plot(listOfT, listOfV, color='forestgreen', marker='.', linewidth=0.5, label='Euler with h = 0.05')

# TODO: Improved Euler.
listOfV = []
listOfT = []

# first step size
improved_euler(t0, v0, tf, stepOne)
pyplot.plot(listOfT, listOfV, color='cornflowerblue', marker='.', linewidth=1.5, label='Improved Euler with h = 0.5')

listOfV = []
listOfT = []

# second step size
improved_euler(t0, v0, tf, stepTwo)
pyplot.plot(listOfT, listOfV, color='royalblue', marker='.', linewidth=0.5, label='Improved Euler with h = 0.05')

# TODO: Runge Kutta.

listOfV = []
listOfT = []

# first step size
runge_kutta(t0, v0, tf, stepOne)
pyplot.plot(listOfT, listOfV, color='lightcoral', marker='.', linewidth=1.5, label='RK with h = 0.5')

listOfV = []
listOfT = []

# second step size
runge_kutta(t0, v0, tf, stepTwo)
pyplot.plot(listOfT, listOfV, color='maroon', marker='.', linewidth=0.5, label='RK with h = 0.05')

pyplot.legend()
pyplot.xlabel('Time')
pyplot.ylabel('Velocity')
pyplot.title('v\'(t) = 9 - 0.2v - 0.27 v^1.5.')

pyplot.tight_layout()  # this method adjusts the graph to the size of the window it's opened in.
pyplot.grid(True)  # This method adds a grid.
pyplot.show()
