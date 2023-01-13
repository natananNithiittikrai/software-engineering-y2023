import statistics as stats

try:
    # Open the file for reading
    with open("Stat.txt", "r") as file:
        # Initialize a list to store the values
        values = []
        # Iterate over the lines in the file
        for line in file:
            # Strip leading/trailing whitespace and convert to a float
            value = float(line.strip())
            # Append the value to the list
            values.append(value)
        # Calculate the standard deviation
        std_dev = stats.stdev(values)
        # Calculate the mean
        mean = stats.mean(values)
        # Calculate the min
        min_value = min(values)
        # Calculate the max
        max_value = max(values)

        print("std: ", std_dev)
        print("mean: ", mean)
        print("min: ", min_value)
        print("max: ", max_value)
except FileNotFoundError:
    print("The file could not be found.")
