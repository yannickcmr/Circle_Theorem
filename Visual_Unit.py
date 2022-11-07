import matplotlib.pyplot as plt
from Calc_Unit import Circle_Theorem, Randomize_Matrix

""" Visualization """

# Splits the tuple of centers and radii into two lists.
def Split_Values(array: list):
    x_values = [x[0] for x in array]
    rad_values = [x[1] for x in array]
    return x_values, rad_values

# returns xlim scale for plotting.
def Get_Scale_x(array):
    range_max = [x[0] + x[1] for x in array]
    range_min = [x[0] - x[1] for x in array]
    return [min(range_min) - 1, max(range_max) + 1]

# returns ylim scale for plotting. Only depends on the radii.
def Get_Scale_y(array):
    range_max = max(array ,key=lambda item:item[1])[1]
    return [-range_max - 1, range_max + 1]

def Visualize_Circle_Theorem(circle_values: list, exact_values: list = []):
    colours = ["blue", "green", "yellow", "orange", "magenta", "brown", "pink", "turquoise"]

    x_val, rad_val = Split_Values(circle_values)
    # initialize plot.
    figure, axes = plt.subplots()
    plt.title("Kreisapproximation der Eingabe")
    plt.grid(True, which="both")
    axes.set_aspect("equal")

    plt.xlim(Get_Scale_x(circle_values))
    plt.ylim(Get_Scale_y(circle_values))

    plt.axhline(linewidth=2, color="black")
    plt.axvline(linewidth=2, color="black")

    # adding the circles in which the eigenvalues lie in.
    for i in range(0, len(x_val)):
        axes.add_artist(plt.Circle((x_val[i], 0), rad_val[i], alpha=0.25, color=colours[i]))
        axes.add_artist(plt.Circle((x_val[i], 0), 0.02, alpha=0.69, color=colours[i]))
    # adding the exact eigenvalues as little red stars if desired.
    if len(exact_values) > 0:
        x_exact, y_exact = Split_Values(exact_values)
        plt.scatter(x_exact, y_exact , color="red", s=25, marker="*", zorder=2)

    plt.show()

if __name__ == "__main__":
    test_matrix = Randomize_Matrix(15, 3)
    print(test_matrix)
    theorem, exact = Circle_Theorem(test_matrix)
    print(f"{theorem}\n{exact}")
    Visualize_Circle_Theorem(theorem, exact)

