from time import monotonic


class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.moves = 0
        self.result = "In progress"
        self.game_time = 0.0


class Checker:
    def __init__(self, color):
        self.color = color
        self.king = False

    def directions(self):
        if self.king:
            return [-1, 1]

        if self.color == "black":
            return [1]

        return [-1]

    def promote(self, row, size):
        if self.color == "black":
            last_row = size - 1
        else:
            last_row = 0

        if row == last_row:
            self.king = True

    def symbol(self):
        if self.color == "black":
            letter = "b"
        else:
            letter = "w"

        if self.king:
            return letter.upper()

        return letter


class Board:
    def __init__(self, size=8):
        if size not in (8, 10):
            raise ValueError("Board size must be 8 or 10.")

        self.size = size
        self.cells = []

        for row in range(size):
            new_row = []

            for col in range(size):
                new_row.append(None)

            self.cells.append(new_row)

        self.forced_piece = None
        self.setup()

    def setup(self):
        rows = self.size // 2 - 1

        for row in range(self.size):
            for col in range(self.size):
                if (row + col) % 2 == 1:
                    if row < rows:
                        self.cells[row][col] = Checker("black")

                    elif row >= self.size - rows:
                        self.cells[row][col] = Checker("white")

    def inside(self, row, col):
        return (
            0 <= row < self.size
            and 0 <= col < self.size
        )

    def display(self):
        print("\n   ", end="")

        for col in range(self.size):
            print(col + 1, end=" ")

        print()

        for row in range(self.size):
            print(f"{row + 1:2} ", end="")

            for col in range(self.size):
                piece = self.cells[row][col]

                if piece is None:
                    print(".", end=" ")
                else:
                    print(piece.symbol(), end=" ")

            print()

    def piece_moves(self, row, col, captures_only=False):
        piece = self.cells[row][col]
        moves = []

        if piece is None:
            return moves

        for direction in piece.directions():
            for sideways in [-1, 1]:
                near_row = row + direction
                near_col = col + sideways

                if not self.inside(near_row, near_col):
                    continue

                neighbor = self.cells[near_row][near_col]

                if neighbor is None:
                    if not captures_only:
                        moves.append(
                            (row, col, near_row, near_col)
                        )

                elif neighbor.color != piece.color:
                    end_row = row + 2 * direction
                    end_col = col + 2 * sideways

                    if self.inside(end_row, end_col):
                        if self.cells[end_row][end_col] is None:
                            moves.append(
                                (row, col, end_row, end_col)
                            )

        return moves

    def legal_moves(self, color):
        if self.forced_piece is not None:
            row, col = self.forced_piece
            piece = self.cells[row][col]

            if piece.color == color:
                return self.piece_moves(row, col, True)

            return []

        moves = []

        for row in range(self.size):
            for col in range(self.size):
                piece = self.cells[row][col]

                if piece is not None:
                    if piece.color == color:
                        moves.extend(
                            self.piece_moves(row, col)
                        )

        captures = []

        for move in moves:
            if abs(move[2] - move[0]) == 2:
                captures.append(move)

        if captures:
            return captures

        return moves

    def move(self, color, move):
        if move not in self.legal_moves(color):
            raise ValueError(
                "Illegal move. Captures and continued jumps "
                "are mandatory."
            )

        row, col, end_row, end_col = move

        piece = self.cells[row][col]
        was_king = piece.king
        captured = abs(end_row - row) == 2

        self.cells[end_row][end_col] = piece
        self.cells[row][col] = None

        if captured:
            middle_row = (row + end_row) // 2
            middle_col = (col + end_col) // 2
            self.cells[middle_row][middle_col] = None

        piece.promote(end_row, self.size)

        promoted = piece.king and not was_king
        self.forced_piece = None

        if captured and not promoted:
            more_captures = self.piece_moves(
                end_row, end_col, True
            )

            if more_captures:
                self.forced_piece = (end_row, end_col)

        return self.forced_piece is None

    def count(self, color):
        total = 0

        for row in self.cells:
            for piece in row:
                if piece is not None:
                    if piece.color == color:
                        total += 1

        return total


class StandardBoard(Board):
    def __init__(self):
        super().__init__(8)


class LargeBoard(Board):
    def __init__(self):
        super().__init__(10)


class Game:
    def __init__(self, first_name, second_name, board):
        self.players = [
            Player(first_name, "black"),
            Player(second_name, "white")
        ]

        self.board = board
        self.current = 0
        self.moves = 0
        self.game_time = 0.0
        self.reason = ""
        self.finished = False

    def finish(self, winner, reason):
        self.finished = True
        self.reason = reason

        for index, player in enumerate(self.players):
            if winner is None:
                player.result = "Stopped"
            elif index == winner:
                player.result = "Won"
            else:
                player.result = "Lost"

    def play_turn(self):
        player = self.players[self.current]

        if not self.board.legal_moves(player.color):
            self.finish(
                1 - self.current,
                "No legal moves remain."
            )
            return

        turn_started = False

        while True:
            print(
                f"\n{player.name} ({player.color})"
                f" - moves: {player.moves}"
            )

            command = input(
                "Enter 'move' or 'finish': "
            ).strip().lower()

            if command == "finish":
                self.finish(
                    None,
                    f"Stopped by {player.name}."
                )
                return

            if command != "move":
                print("Please enter move or finish.")
                continue

            try:
                values = input(
                    "From row col to row col "
                    "(example: 3 2 4 1), or finish: "
                ).strip().lower()

                if values == "finish":
                    self.finish(
                        None,
                        f"Stopped by {player.name}."
                    )
                    return

                numbers = values.split()

                if len(numbers) != 4:
                    raise ValueError(
                        "Enter exactly four numbers."
                    )

                move = (
                    int(numbers[0]) - 1,
                    int(numbers[1]) - 1,
                    int(numbers[2]) - 1,
                    int(numbers[3]) - 1
                )

                turn_done = self.board.move(
                    player.color, move
                )

            except ValueError as error:
                print(f"Invalid input: {error}")
                continue

            if not turn_started:
                player.moves += 1
                self.moves += 1
                turn_started = True

            row, col, end_row, end_col = move

            print(
                f"{player.name} ({player.color}) moved: "
                f"({row + 1}, {col + 1}) -> "
                f"({end_row + 1}, {end_col + 1})"
            )

            self.board.display()

            if turn_done:
                self.current = 1 - self.current
                return

            print(
                "Continue jumping with the same piece, "
                "or finish the game."
            )

    def summary(self):
        print(f"\nGame over: {self.reason}")
        print(f"Total moves: {self.moves}")
        print(
            f"Game duration: {self.game_time:.1f} seconds"
        )

        for player in self.players:
            print(f"\nPlayer: {player.name}")
            print(f"Color: {player.color}")
            print(f"Moves: {player.moves}")
            print(f"Result: {player.result}")
            print(
                "Remaining pieces:",
                self.board.count(player.color)
            )
            print(
                f"Game time: {player.game_time:.1f} seconds"
            )

    def run(self):
        started = monotonic()
        self.board.display()

        try:
            while not self.finished:
                self.play_turn()

        except (EOFError, KeyboardInterrupt):
            self.finish(None, "Input interrupted.")

        self.game_time = monotonic() - started

        for player in self.players:
            player.game_time = self.game_time

        self.summary()


def main():
    try:
        first = input(
            "Black player name: "
        ).strip() or "Player 1"

        second = input(
            "White player name: "
        ).strip() or "Player 2"

        choice = input(
            "Board: 8 (standard) or 10 (practice) [8]: "
        ).strip() or "8"

        while choice not in ("8", "10"):
            choice = input(
                "Please enter 8 or 10: "
            ).strip()

    except (EOFError, KeyboardInterrupt):
        print("\nSetup cancelled.")
        return

    if choice == "8":
        board = StandardBoard()
    else:
        board = LargeBoard()

    game = Game(first, second, board)
    game.run()


if __name__ == "__main__":
    main()
