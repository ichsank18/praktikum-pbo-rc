import random

def create_board():
    return [['?' for _ in range(3)] for _ in range(3)]

def place_bomb(board):
    bomb_row, bomb_col = random.randint(0, 2), random.randint(0, 2)
    return bomb_row, bomb_col

def display_board(board):
    for row in board:
        print(' '.join(row))
    print()

def check_win(board, bomb_row, bomb_col):
    return all(board[i][j] != '?' or (i, j) == (bomb_row, bomb_col) for i in range(3) for j in range(3))

def main():
    print("Menangkan tanpa terkena bom dengan mengisi angka 0-2 dan berisi 'Baris spasi Kolom'")
    board = create_board()
    bomb_row, bomb_col = place_bomb(board)
    while True:
        display_board(board)
        try:
            row, col = map(int, input("Masukkan koordinat(ex:1 2): ").split())
            if board[row][col] == '?':
                if (row, col) == (bomb_row, bomb_col):
                    print("Ada bom. GAME  OVER!")
                    board[bomb_row][bomb_col] = 'X'
                    display_board(board)
                    break
                print("aman, lanjutkan.")
                board[row][col] = 'O'
                if check_win(board, bomb_row, bomb_col):
                    print("Anda menang!")
                    break
            else:
                print("Kotak tersebut telah dibuka!")
        except (ValueError, IndexError):
            print("Masukkan angka 0-2 untuk baris dan kolom, misalnya 0 1.")

if __name__ == "__main__":
    main()