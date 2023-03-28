class Snake:
    def __init__(self, init_body, init_direction):
        self.body = init_body
        self.direction = init_direction

    def take_step(self, position):
        self.body = self.body[1:] + [position]

    def set_direction(self, direction):
        self.direction = direction

    def head(self):
        return self.body[-1]

# class Apple:
        
# Gamestate Class
class Game:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    # Initialize Board
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.snake = Snake([(0,0), (1,0), (2,0), (3,0)], 'UP')

    def __repr__(self) -> str:
        return f"{type(self).__name__}(Height:{self.height}, Width:{self.width})"
    
    def board_matrix(self):
        board = [[' ' for col in range(self.width)] for row in range(self.height)]

        # Add Walls to the Board
        for row in range(len(board)):
            if row == 0 or row == len(board)-1:
                board[row][0] = '+'
                for col in range(1, len(board[row]) - 1):
                    board[row][col] = '-'
                board[row][len(board[row]) - 1] = '+'
            else:
                board[row][0] = '|'
                board[row][len(board[row])-1] = '|'

        return board

    def render(self):
        matrix = self.board_matrix()

        # Add Snake to Board
        for bodypart in self.snake.body:
            if bodypart == self.snake.head():
                bodyX, bodyY = bodypart
                bodyX = bodyX + 1
                bodyY = (bodyY - len(matrix)+2) * -1
                print(f'y: {bodyY} x: {bodyX}')
                matrix[bodyY][bodyX] = 'X'
            else:
                bodyX, bodyY = bodypart
                bodyX = bodyX + 1
                bodyY = (bodyY - len(matrix)+2) * -1
                print(f'y: {bodyY} x: {bodyX}')
                matrix[bodyY][bodyX] = '0'

        # Render Board
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                print(matrix[row][col], end='')
            print()


def main():
    game = Game(10, 20)
    # print(game)
    game.render()

if __name__ == "__main__":
    main()