import numpy as np

def calculate(list):
    if(len(list) != 9):
        raise ValueError("There must be 9 elements.")
    list = np.array(list)
    print(list)
    
    
    #mean
    axis1_mean = ([list[[0,3,6]].mean()], [list[[1,4,7]].mean()], [list[[2,5,8]].mean()])
    axis2_mean = ([list[[0,1,2]].mean()], [list[[3,4,5]].mean()], [list[[6,7,8]].mean()])
    flattened_mean = list.mean()

    #var
    axis1_var = ([list[[0,3,6]].var()], [list[[1,4,7]].var()], [list[[2,5,8]].var()])
    axis2_var = ([list[[0,1,2]].var()], [list[[3,4,5]].var()], [list[[6,7,8]].var()])
    flattened_var = list.var()
    
    #std
    axis1_std = ([list[[0,3,6]].std()], [list[[1,4,7]].std()], [list[[2,5,8]].std()])
    axis2_std = ([list[[0,1,2]].std()], [list[[3,4,5]].std()], [list[[6,7,8]].std()])
    flattened_std = list.std()
    
    #max
    axis1_max = ([list[[0,3,6]].max()], [list[[1,4,7]].max()], [list[[2,5,8]].max()])
    axis2_max = ([list[[0,1,2]].max()], [list[[3,4,5]].max()], [list[[6,7,8]].max()])
    flattened_max = list.max()
    
    #min
    axis1_min = ([list[[0,3,6]].min()], [list[[1,4,7]].min()], [list[[2,5,8]].min()])
    axis2_min = ([list[[0,1,2]].min()], [list[[3,4,5]].min()], [list[[6,7,8]].min()])
    flattened_min = list.min()
    
    #sum
    axis1_sum = ([list[[0,3,6]].sum()], [list[[1,4,7]].sum()], [list[[2,5,8]].sum()])
    axis2_sum = ([list[[0,1,2]].sum()], [list[[3,4,5]].sum()], [list[[6,7,8]].sum()])
    flattened_sum = list.sum()

    return {
        'mean': [axis1_mean, axis2_mean, flattened_mean],
        'variance': [axis1_var, axis2_var, flattened_var],
        'standard deviation': [axis1_std, axis2_std, flattened_std],
        'max': [axis1_max, axis2_max, flattened_max],
        'min': [axis1_min, axis2_min, flattened_min],
        'sum': [axis1_sum, axis2_sum, flattened_sum]
}

print(calculate([0,1,2,3,4,5,6,7,8]))