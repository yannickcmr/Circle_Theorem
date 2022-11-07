import matplotlib.pyplot as plt
from Calc_Unit import Circle_Theorem, Randomize_Matrix

""" Visualization """

def Split_Values(array: list):
    x_values = [x[0] for x in array]
    y_values = [x[1] for x in array]
    return x_values, y_values

def Get_Scale(array):
    range_max = [x[0] + x[1] for x in array]
    range_min = [x[0] - x[1] for x in array]
    return [min(range_min), max(range_max)]

def Visualize_Circle_Theorem(circle_values: list, exact_values: list = []):
    colours = ["blue", "green", "yellow", "orange", "magenta", "brown"]
    
    x_val, y_val = Split_Values(circle_values)
    figure, axes = plt.subplots()

    for i in range(0, len(x_val)):
        axes.add_artist(plt.Circle((x_val[i], 0), y_val[i], alpha=0.25, color=colours[i]))
        axes.add_artist(plt.Circle((x_val[i], 0), 0.02, alpha=0.69, color=colours[i]))

    if len(exact_values) > 0:
        x_exact, y_exact = Split_Values(exact_values)
        plt.scatter(x_exact, y_exact , color="red")

    axes.set_aspect("equal")
    plt.title("Kreisapproximation der Eingabe")
    plt.grid(True, which="both")

    plt.xlim(Get_Scale(circle_values))
    plt.ylim(Get_Scale(circle_values))

    plt.axhline(linewidth=2, color="black")
    plt.axvline(linewidth=2, color="black")
    plt.show()

if __name__ == "__main__":
    test_matrix = Randomize_Matrix(2, 2)
    print(test_matrix)
    theorem, exact = Circle_Theorem(test_matrix)
    print(theorem)
    Visualize_Circle_Theorem(theorem, exact)

