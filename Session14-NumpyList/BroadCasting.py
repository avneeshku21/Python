# *Broadcasting

# The term broadcasting describes how NumPy treats arrays with different shapes during arithmetic operations.

# The smaller array is “broadcast” across the larger array so that they have compatible shapes.

# Broadcasting Rules
# 1. Make the two arrays have the same number of dimensions.

# If the numbers of dimensions of the two arrays are different, add new dimensions with size 1 to the head of the array with the smaller dimension.
# 2. Make each dimension of the two arrays the same size.

# If the sizes of each dimension of the two arrays do not match, dimensions with size 1 are stretched to the size of the other array.
# If there is a dimension whose size is not 1 in either of the two arrays, it cannot be broadcasted, and an error is raised.
