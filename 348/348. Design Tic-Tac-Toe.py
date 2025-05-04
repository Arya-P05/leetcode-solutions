from typing import List

class TicTacToe:
    def init(self, n: int) -> None:
        self.p1_symbol = "X"
        self.p2_symbol = "O"
        self.board = [["" for _ in range(n)] for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        
        if player == 1:
            self.board[row][col] = self.p1_symbol
        else:
            self.board[row][col] = self.p2_symbol

        winner = self.check_winner(player)

        if winner == 1 or winner == 2:
            return winner
        else: 
            return 0
    
    def check_winner(self, player: int) -> int:
        if self.check_rows(player) or self.check_cols(player) or self.check_diagonals(player):
            return player

        else:
            return 0
    
    def check_rows(self, player: int) -> bool:
        symbol = self.p1_symbol if player == 1 else self.p2_symbol

        for row in self.board:
            if all(cell == symbol for cell in row):
                return True
        
        return False
    
    def check_cols(self, player: int) -> bool:
        symbol = self.p1_symbol if player == 1 else self.p2_symbol

        for col in range(len(self.board)):
            if all(row[col] == symbol for row in self.board):
                return True
            
        return False
    
    def check_diagonals(self, player: int) -> bool:
        symbol = self.p1_symbol if player == 1 else self.p2_symbol

        n = len(self.board)
        
        if all(self.board[i][i] == symbol for i in range(n)) or all(self.board[i][n - 1 - i] == symbol for i in range(n)):
            return True
        
        return False


