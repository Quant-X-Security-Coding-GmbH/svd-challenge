import scipy
from svd_challenge import SVD
from timer import Timer

''' For some reason this file executes all methods that would be executed by the svd_challenge.py file when run. '''
timed = Timer()


def looping_application():
    a = 50
    b = a
    five = True

    while (a * b) <= 500000000:  # ~6.5GiB RAM needed to compute max size. 6.5 GiB RAM ~ 500,000,000 computed elements
        for i in range(2):
            if i == 0:
                d = 0.1
            else:
                d = 0.25
            for j in range(3):
                b = a
                if j == 1:
                    b = a/2
                elif j == 2:
                    b = a/10
                try:
                    # Creating new matrix for each iteration
                    A = SVD().random_s_matrix(a, b, d, "binary")

                    # Print dimensions
                    print(
                        "m: " + str(a),
                        "n: " + str(b)
                    )

                    # Print density
                    print("Density: " + str(d))

                    try:
                        # Print min/max singular value
                        largest, smallest = SVD().decomposition_singular_values(A)
                        print(
                            "Max Singular Value: " + str(largest),
                            "Min Singular Value: " + str(smallest)
                        )

                        # Print condition number
                        print("Condition Number: " + str(SVD().cond_num(largest, smallest)))

                    except scipy.sparse.linalg.eigen.ArpackNoConvergence:
                        print("Could not find smallest singular value.")

                    # Print computation time
                    timed.start()
                    try:
                        SVD().decomposition_singular_values(A)
                    except scipy.sparse.linalg.eigen.ArpackNoConvergence:
                        pass
                    SVD().cond_num(largest, smallest)
                    timed.stop()

                    print("")

                except MemoryError:
                    print("Not enough memory!")
                    return
        if five:
            a *= 2
            five = False
        else:
            a *= 5
            five = True
    return


looping_application()
