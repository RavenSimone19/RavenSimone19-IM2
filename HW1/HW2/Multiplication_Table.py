def search_matrix():
    while True:
        try:
            row = int(input("Enter row: "))
            col = int(input("Enter col: "))
            search_val = int(input("Search: "))
        except ValueError:
            print("Invalid input. Please enter integers only.")
            continue

        if row <= 0 or col <= 0:
            print("Stop the loop")
            break

        matrix = [[i * j for j in range(1, col + 1)] for i in range(1, row + 1)]

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == search_val:
                    print(f"[{matrix[i][j]}]", end=" ")
                else:
                    print(matrix[i][j], end=" ")
            print()

search_matrix()