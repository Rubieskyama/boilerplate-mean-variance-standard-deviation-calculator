import numpy as np

def calculate(lst):
    # Check if the length of input is 9
    if len(lst) != 9:
        raise ValueError('List must contain nine numbers.')
    # Convert input into a 3*3 array
    matrix = np.array(lst).reshape(3,3)
    
    # Calculate mean
    mean_axis0 = matrix.mean(axis=0).tolist()
    mean_axis1 = matrix.mean(axis=1).tolist()
    mean_flattened = matrix.mean().tolist()

    # Calculate variance
    var_axis0 = matrix.var(axis=0).tolist()
    var_axis1 = matrix.var(axis=1).tolist()
    var_flattened = matrix.var().tolist()

    # Calculate standard deviation
    std_axis0 = matrix.std(axis=0).tolist()
    std_axis1 = matrix.std(axis=1).tolist()
    std_flattened = matrix.std().tolist()

    # Calculate maximum
    max_axis0 = matrix.max(axis=0).tolist()
    max_axis1 = matrix.max(axis=1).tolist()
    max_flattened = matrix.max().tolist()

    # Calculate minimum
    min_axis0 = matrix.min(axis=0).tolist()
    min_axis1 = matrix.min(axis=1).tolist()
    min_flattened = matrix.min().tolist()

    # Calculate the sum
    sum_axis0 = matrix.sum(axis=0).tolist()
    sum_axis1 = matrix.sum(axis=1).tolist()
    sum_flattened = matrix.sum().tolist()

    # Return results as a dictionary
    calculations = {
        'Mean':[mean_axis0,mean_axis1,mean_flattened],
        'Variance':[var_axis0,var_axis1,var_flattened],
        'Standard deviation':[std_axis0,std_axis1,std_flattened],
        'Max':[max_axis0,max_axis1,max_flattened],
        'Min':[min_axis0,min_axis1,min_flattened],
        'Sum':[sum_axis0,sum_axis1,sum_flattened]
    }

    return calculations