import random

ROWS = 15
COLUMNS = 15

def generate_path_y():

    matrix = [[0] * COLUMNS for _ in range(ROWS)]

    path_y = 0
    path_x = random.randint(0, COLUMNS - 1)
    matrix[path_y][path_x] = 1

    while path_y < ROWS - 1:

        forward = False
        previous_direction = None

        while forward is False:

            # Left, right, or forward
            if path_x > 0 and path_x < COLUMNS - 1 and previous_direction is None:
                new_path = random.randint(0, 2)

            # Left or forward
            elif path_x == COLUMNS - 1 or previous_direction == "right":
                new_path = random.randint(0, 1)

            # Right or forward
            elif path_x == 0 or previous_direction == "left":
                new_path = random.randint(1, 2)

            if new_path == 0:
                path_x -= 1
                previous_direction = "right"

            elif new_path == 2:
                path_x += 1
                previous_direction = "left"

            else:
                path_y += 1
                forward = True

            matrix[path_y][path_x] = 1

    print_matrix(matrix)


def generate_path_x():

    matrix = [[0] * COLUMNS for _ in range(ROWS)]

    path_y = random.randint(0, ROWS - 1)
    path_x = 0
    matrix[path_y][path_x] = 1

    while path_x < COLUMNS - 1:

        forward = False

        while forward is False:

            # Up, down, or forward
            if path_y > 0 and path_y < ROWS - 1:
                new_path = random.randint(0, 2)

            #  Up or forward
            elif path_y == COLUMNS - 1:
                new_path = random.randint(0, 1)

            # Down or forward
            elif path_y == 0:
                new_path = random.randint(1, 2)

            if new_path == 0:
                path_y -= 1

            elif new_path == 2:
                path_y += 1

            else:
                path_x += 1
                forward = True

            matrix[path_y][path_x] = 1

    print_matrix(matrix)


def print_matrix(array):
    
    for i in range(len(array)):

        for j in range(len(array)):

            print(array[i][j], end=" ")

        print("")


if __name__ == '__main__':
    generate_path_x()