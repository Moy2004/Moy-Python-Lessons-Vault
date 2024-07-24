"""
2024 - 7 - 24
1446 ٱلْمُحَرَّم 18

Mean-Variance-Standard Deviation Calculator
"""
# import files
import numpy as np

# initial data generation
List = np.random.randint(0, 128, size=(3, 3), dtype='int8')
List_Flat = np.ndarray.flatten(List)

print(List)
print(List_Flat)


# Calculate Function
def Calculate(List, Flat):
    if len(Flat) != 9:
        raise ValueError("The list may have more/less items then 9")


    def mean():
        mean_ax1 = np.mean(List[:, 0]).item()
        mean_ax2 = np.mean(List[:, 1]).item()
        mean_all = np.mean(Flat).item()

        return mean_ax1, mean_ax2, mean_all

    def var():
        var_ax1 = np.var(List[:, 0]).item()
        var_ax2 = np.var(List[:, 1]).item()
        var_all = np.var(Flat).item()

        return var_ax1, var_ax2, var_all

    def std():
        std_ax1 = np.std(List[:, 0]).item()
        std_ax2 = np.std(List[:, 1]).item()
        std_all = np.std(Flat).item()

        return std_ax1, std_ax2, std_all

    def max():
        max_ax1 = np.max(List[:, 0]).item()
        max_ax2 = np.max(List[:, 1]).item()
        max_all = np.max(Flat).item()

        return max_ax1, max_ax2, max_all

    def min():
        min_ax1 = np.min(List[:, 0]).item()
        min_ax2 = np.min(List[:, 1]).item()
        min_all = np.min(Flat).item()

        return min_ax1, min_ax2, min_all

    def sum():
        sum_ax1 = np.sum(List[:, 0]).item()
        sum_ax2 = np.sum(List[:, 1]).item()
        sum_all = np.sum(Flat).item()

        return sum_ax1, sum_ax2, sum_all

    output = {
        'mean': mean(),
        'variance': var(),
        'standard deviation': std(),
        'max': max(),
        'min': min(),
        'sum': sum()
    }

    print(output)


Calculate(List, List_Flat)
