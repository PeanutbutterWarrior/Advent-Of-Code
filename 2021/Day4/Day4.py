with open("Day4.txt", "r") as file:
    data = file.read()

calls, *raw_boards = data.split('\n\n')
calls = [int(i) for i in calls.split(',')]

boards = []
for raw_board in raw_boards:
    if not raw_board:
        continue
    board = []
    for num in raw_board.split():
        if num:
            board.append(int(num))
    boards.append(board)

found_first_finish = True
board_count = len(boards)
for call in calls:
    for board in boards:
        if not board:
            continue

        for ind, val in enumerate(board):
            if val == call:
                board[ind] = None
        for i in range(5):
            row_finished = True
            column_finished = True
            for j in range(5):
                if board[i * 5 + j] is not None:
                    row_finished = False
                if board[i + j * 5] is not None:
                    column_finished = False
            if row_finished or column_finished:
                if found_first_finish:
                    found_first_finish = False
                    print(sum(filter(lambda i: i is not None, board)) * call)
                if board_count == 1:
                    print(sum(filter(lambda i: i is not None, board)) * call)
                    quit()
                board.clear()
                board_count -= 1
                break
