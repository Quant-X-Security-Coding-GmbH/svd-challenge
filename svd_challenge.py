from scipy import *
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

# Singular value decomposition. The command linalg.svd will return U,V^H,
# and o as an array of the singular values. To obtain the matrix Σ, use
# linalg.diagsvd. The following example illustrates the use of linalg.svd:
def decompositionSingular():
    A = np.array([[1, 2, 3], [4, 5, 6]])
    M, N = A.shape
    U, s, Vh = linalg.svd(A)
    Sig = linalg.diagsvd(s, M, N)
    U, Vh = U, Vh
    print(U)
    print(Sig)
    print(Vh)
    print(U.dot(Sig.dot(Vh)))  #check computation
