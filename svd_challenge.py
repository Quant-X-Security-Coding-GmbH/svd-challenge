import numpy as np
import scipy.sparse.linalg as sparse, scipy.stats as stats, scipy.sparse

from timer import Timer
# import matplotlib.pyplot as plt


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


svd_timer = Timer()


class SVD(object):

    def random_s_matrix(self, m, n, dens, value_type, r_seed=None, location=0, scl=100):
        # Creates a random matrix with fixed dimensions, sparsity, and further features
        ''' DOES NOT ACCEPT FLOAT VALUES FOR DIMENSIONS (m, n)
            due to the usage of scipy.sparse.random() as well as simple mathematics '''

        if r_seed:
            np.random.seed(r_seed)

        try:
            if value_type == "binary":
                matrix = scipy.sparse.random(
                    int(m),
                    int(n),
                    density=dens,
                    data_rvs=np.ones
                )

            elif value_type == "float":
                matrix = scipy.sparse.random(
                    int(m),
                    int(n),
                    density=dens,
                    data_rvs=stats.norm(
                        loc=location,
                        scale=scl
                    ).rvs
                )

            return matrix

        except ValueError:
            print("A problem occurred. To call this function, the following arguments can be used:"
                  " random_s_matrix(m, n, density, value_type, *random_seed, *location, *scale)")
            return

    def decomposition_singular_values(self, A):
        U, s, Vh = sparse.svds(A, k=1, which='LM')
        U, s2, Vh = sparse.svds(A, k=1, which='SM')  # ARPACK error sometimes traces back to this line; e.g.:
        return s, s2                                 # ARPACK error -1: No convergence (5001 iterations, 0/1
                                                     # eigenvectors converged)

    def cond_num(self, sin, sin2):
        # Computes the condition number
        if sin2 != 0:
            c = sin/sin2
        else:
            c = "inf"
        return c


# A = SVD().random_s_matrix(485, 485, 0.1, value_type="binary")
''' 13 x 7 seem to be the standard minimum dimensions required for the use of scipy.linalg.sparse.svds().
    This changes relative to what k (number of singular values/vectors to be computed) is defined as during the 
    usage of scipy...svds(). If k is not defined by the user, it is set as k=6. The ArpackNoConvergence error starts
    occurring at approximately {485 x 485} dimensions for the matrix. '''

# svd_timer.start()
# SVD().cond_num(SVD().decomposition_singular_values(A))
# svd_timer.stop()
# try:
#   z, z2 = SVD().decomposition_singular_values(A)
#   print(SVD().cond_num(z, z2))
# except scipy.sparse.linalg.eigen.ArpackNoConvergence:
#   pass

# print(random_s_matrix(10, 10, 0.25, "binary", r_seed=15).toarray())
# plt.imshow(A.toarray())
# plt.show()


