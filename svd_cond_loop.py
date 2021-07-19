from svd_challenge import SVD
from timer import Timer


svd_timer = Timer()

def looping_application():
    a = 50
    b = a
    five = True

    while (a * b) <= 500000000:
        for i in range(1):
            if i == 0:
                d = 0.1
            else:
                d = 0.25
            for j in range(2):
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

                    # Print min/max singular value
                    print(
                        "Max Singular Value: " + str(max(SVD().decomposition_singular_values(A))),
                        "; Min Singular Value: " + str(min(SVD().decomposition_singular_values(A)))
                    )

                    # Print condition number
                    print("Condition Number: " + str(SVD().cond_num(SVD().decomposition_singular_values(A))))

                    # Print computation time
                    svd_timer.start()
                    SVD().cond_num(SVD().decomposition_singular_values(A))
                    svd_timer.stop()

                    print("")

                except MemoryError:
                    print("Not enough memory!")
                    return
        if five:
            a *= 2
        else:
            a *= 5
            five = True
    return


looping_application()
