import numpy as np
import scipy.sparse.linalg as sparse, scipy.stats as stats, scipy.sparse
#import matplotlib.pyplot as plt
#from timer import *
from scipy import linalg


# Copyright [yyyy] [name of copyright owner]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Things to do:
 - Please name this file <demo_name>.py
 - Fill in [yyyy] and [name of copyright owner] in the copyright (top line)
 - Add demo code below
 - Format code so that it conforms with PEP 8
"""


def random_s_matrix(matrix, dimension_x, dimension_y, dens, value_type, r_seed=None, location=0, scl=100):

    if r_seed:
        np.random.seed(r_seed)

    try:
        if value_type == "binary":
            matrix = scipy.sparse.random(
                dimension_x,
                dimension_y,
                density=dens,
                data_rvs=np.ones
            )

        elif value_type == "float":
            matrix = scipy.sparse.random(
                dimension_x,
                dimension_y,
                density=dens,
                data_rvs=stats.norm(
                    loc=location,
                    scale=scl
                ).rvs
            )

        return matrix

    except ValueError:
        print("A problem occurred. To call this function, the following arguments can be used:"
              "random_s_matrix(matrix, m, n, density, value_type, *random_seed, *location, *scale)")
        return


def decomposition_singular(A):
    M, N = A.shape
    U, s, Vh = sparse.svds(A)
    return s


def cond_num(s):
    # Computes the condition number
    c = s[-1]/s[0]
    return c


np.random.seed(25)
A = scipy.sparse.random(50, 50, density=0.25, data_rvs=np.ones)  # binary

# B = scipy.sparse.random(50, 50, density=0.25, data_rvs=stats.norm(loc=0, scale=100).rvs)  # float values
                       # n x m,   sparsity,         location and range of matrix values


print(cond_num(decomposition_singular(A)))
# print(A.toarray())
# plt.imshow(A.toarray())
# plt.show()


decomposition_singular(A)