class ChessGame:
    def __init__(self):
        self.board = self.create_board()
        self.current_turn = "white"
        self.moves_history = []

    def create_board(self):
        # Create an 8x8 chess board with pieces in their initial positions
        board = [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"]
        ]
        return board

    def print_board(self):
        # Print the current state of the board
        print("   a b c d e f g h")
        print("  -----------------")
        for i in range(8):
            print(f"{8 - i} | {' '.join(self.board[i])} | {8 - i}")
        print("  -----------------")
        print("   a b c d e f g h")

    def move_piece(self, start, end):
        # Move a piece from start position to end position
        start_row, start_col = self.position_to_indices(start)
        end_row, end_col = self.position_to_indices(end)

        piece = self.board[start_row][start_col]
        self.board[start_row][start_col] = " "
        self.board[end_row][end_col] = piece

        self.moves_history.append((start, end))

    def position_to_indices(self, position):
        # Convert chess notation (e.g., 'e2') to board indices (row, column)
        col_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        col = col_map[position[0]]
        row = 8 - int(position[1])
        return row, col

    def play(self):
        # Main game loop
        while True:
            self.print_board()
            print(f"\n{self.current_turn.capitalize()}'s turn.")
            start = input("Enter the starting position of the piece (e.g., e2): ")
            end = input("Enter the ending position of the piece (e.g., e4): ")

            self.move_piece(start, end)

            # Switch turns
            self.current_turn = "black" if self.current_turn == "white" else "white"

            # Clear screen for the next turn (for better visualization)
            print("\n" * 100)

# Run the game
if __name__ == "__main__":
    game = ChessGame()
    game.play()
