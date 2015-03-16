import numpy as np
from __future__ import division
class Transformations(object):
    """since these transformations are all related, we'll nest them all under a feature norm class"""
    def mean_at_zero(self, arr):
        return np.array([i - np.mean(a) for i in arr])

    def norm_to_min_zero(self, arr):
        return np.array([i / max(a) for i in arr])
    
    def norm_to_absolute_min_zero(self, arr):
        """should be a range of 0 to 1, where 0 maintains its 0 value"""
        return np.array([(i-min(arr))/(max(arr)-min(arr)) for i in arr])
    
    def norm_to_neg_pos(self, arr):
        """should be a range of -1 to 1, where 0 represents the mean"""
        return np.array([(i-mean(arr))/(max(arr)-mean(arr)) for i in arr])
    
    def norm_by_std(self, arr):
        """should be a range where 0 represents the mean"""
        return np.array([(i-mean(arr))/std(arr) for i in arr])
