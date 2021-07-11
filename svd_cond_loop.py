from svd_challenge import decomposition_singular_values, random_s_matrix, cond_num, svd_timer

matrix_list = [
    {"n": 50, "m": 50, "density": 0.1},
    {"n": 50, "m": 10, "density": 0.1},
    {"n": 50, "m": 50, "density": 0.25},
    {"n": 50, "m": 10, "density": 0.25},
    {"n": 100, "m": 100, "density": 0.1},
    {"n": 100, "m": 50, "density": 0.1},
    {"n": 100, "m": 10, "density": 0.1},
    {"n": 100, "m": 100, "density": 0.25},
    {"n": 100, "m": 50, "density": 0.25},
    {"n": 100, "m": 10, "density": 0.25},
    {"n": 1000, "m": 1000, "density": 0.1},
    {"n": 1000, "m": 500, "density": 0.1},
    {"n": 1000, "m": 100, "density": 0.1},
    {"n": 1000, "m": 1000, "density": 0.25},
    {"n": 1000, "m": 500, "density": 0.25},
    {"n": 1000, "m": 100, "density": 0.25},
    {"n": 10000, "m": 10000, "density": 0.1},
    {"n": 10000, "m": 5000, "density": 0.1},
    {"n": 10000, "m": 1000, "density": 0.1},
    {"n": 10000, "m": 10000, "density": 0.25},
    {"n": 10000, "m": 5000, "density": 0.25},
    {"n": 10000, "m": 1000, "density": 0.25},
    {"n": 100000, "m": 100000, "density": 0.1},
    {"n": 100000, "m": 50000, "density": 0.1},
    {"n": 100000, "m": 10000, "density": 0.1},
    {"n": 100000, "m": 100000, "density": 0.25},
    {"n": 100000, "m": 50000, "density": 0.25},
    {"n": 100000, "m": 10000, "density": 0.25}
    ]


def looping_application(dic):
    i = 0
    while i <= int(len(dict)-1):
        # Creating new matrix for each iteration
        A = random_s_matrix(m=dic[i]["m"], n=dic[i]["n"], dens=dic[i]["density"], value_type="binary")

        # Print dimensions
        print(
            "m: " + str(dic[i]["m"]),
            "n: " + str(dic[i]["n"])
        )

        # Print density
        print("Density: " + str(dic[i]["density"]))

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

        i += 1

    return


looping_application(matrix_list)
