import matplotlib.pyplot as plt
from pyne import nucname

def nuclide_chart_plot(nuclide_datamap):
    """Generate a plot of data, provided per nuclide, in a visualiation
    that looks like a typical chart of the nuclides.
    
    input
    -----
    nuclide_datamap: dict(nucname: doube) 
                     provides data for each of a set of nuclides given as nucnames
    """

    plot_data = []
    for nuclide, data in nuclide_datamap:
        Z = nuclide.znum()
        N = nuclide.anum() - Z
        plot_data.append((Z,N,data))
    x, y, c = zip(*plot_data)
    plt.figure(figsize=(12, 8))
    plt.scatter(x, y, c=c, marker="s", s=6)
    plt.title("Chart of the nuclides")
    plt.xlabel("Number of neutrons (N)")
    plt.ylabel("Number of protons (Z)")
    plt.show()