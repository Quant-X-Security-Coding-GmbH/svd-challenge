from svd_challenge import decomposition_singular_values, random_s_matrix, cond_num, svd_timer


def looping_application():
    i = 0
    j = 0
    a = 50
    b = a
    five = True
    while (a * b) <= 50000:
        if j == 0:
            d = 0.1
        else:
            d = 0.25
        if i == 1:
            b = a/2
            i = 0
        else:
            b = a/10
            i = 1
            if j == 0:
                j = 1
            else:
                j = 0
                if five:
                    a *= 2
                    five = False
                else:
                    a *= 5
                    five = True
        try:
            # Creating new matrix for each iteration
            A = random_s_matrix(m=a, n=b, dens=d, value_type="binary")

            # Print dimensions
            print(
                "m: " + str(a),
                "n: " + str(b)
            )

            # Print density
            print("Density: " + str(d))

            # Print min/max singular value
            print(
                "Max Singular Value: " + str(max(decomposition_singular_values(A))),
                "Min Singular Value: " + str(min(decomposition_singular_values(A)))
            )

            # Print condition number
            print("Condition Number: " + str(cond_num(decomposition_singular_values(A))))

            # Print computation time
            svd_timer.start()
            cond_num(decomposition_singular_values(A))
            svd_timer.stop()

            print("")

        except MemoryError:
            return
    return


looping_application()
