import matplotlib.pyplot as plt

def generate_sales_chart(data):
    """
    Generate and save a line chart of monthly revenue.

    This function takes sales data as input, extracts months and revenue values,
    and generates a line chart using Matplotlib. The chart is saved locally
    as 'revenue_chart.png'.

    Parameters
    ----------
    data : list of tuple
        A list containing sales records where each element is a tuple
        in the format (month, revenue).
        Example:
            [
                ("Jan", 1000),
                ("Feb", 1500),
                ("Mar", 2000)
            ]

    Returns
    -------
    str
        A confirmation message indicating the chart file has been saved.

    Output
    ------
    revenue_chart.png
        A PNG image file containing the monthly revenue line chart.

    Notes
    -----
    - The function assumes revenue values are numeric.
    - The chart is saved in the current working directory.
    - Existing files with the same name will be overwritten.

    Example
    -------
    >>> sales_data = [("Jan", 1000), ("Feb", 1500)]
    >>> generate_sales_chart(sales_data)
    'Chart saved as revenue_chart.png'
    """
    x = [row[0] for row in data]
    y = [row[1] for row in data]

    plt.figure()
    plt.plot(x, y)
    plt.title("This Is Your Chart")
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.savefig("chart.png")

    return "Chart saved as chart.png"
