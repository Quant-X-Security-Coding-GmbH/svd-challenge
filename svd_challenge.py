import numpy as np
import scipy.sparse.linalg as sparse, scipy.stats as stats, scipy.sparse
from timer import Timer
# import matplotlib.pyplot as plt


# Copyright 2021 Quant-X Security & Coding GmbH, Germany
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


def random_s_matrix(m, n, dens, value_type, r_seed=None, location=0, scl=100):
    # Creates a random matrix with fixed dimensions, sparsity, and further features

    if r_seed:
        np.random.seed(r_seed)

    try:
        if value_type == "binary":
            matrix = scipy.sparse.random(
                m,
                n,
                density=dens,
                data_rvs=np.ones
            )

        elif value_type == "float":
            matrix = scipy.sparse.random(
                m,
                n,
                density=dens,
                data_rvs=stats.norm(
                    loc=location,
                    scale=scl
                ).rvs
            )

        return matrix

    except ValueError:
        print("A problem occurred. To call this function, the following arguments can be used:"
              "random_s_matrix(m, n, density, value_type, *random_seed, *location, *scale)")
        return


def decomposition_singular_values(A):
    U, s, Vh = sparse.svds(A)
    return s


def cond_num(s):
    # Computes the condition number
    c = s[-1]/s[0]
    return c


A = random_s_matrix(10, 10, 0.25, value_type="binary", r_seed=15)

svd_timer.start()
cond_num(decomposition_singular_values(A))
svd_timer.stop()

print(cond_num(decomposition_singular_values(A)))
# print(random_s_matrix(10, 10, 0.25, "binary", r_seed=15).toarray())
# plt.imshow(A.toarray())
# plt.show()


