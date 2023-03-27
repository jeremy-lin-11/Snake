# class Snake:
        

# class Apple:
        
# Gamestate Class
class Game:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    # Initialize Board
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __repr__(self) -> str:
        return f"{type(self).__name__}(Height:{self.height}, Width:{self.width})"
    
    def board_matrix(self):
        board = [[' ' for x in range(self.width)] for y in range(self.height)]
        return board

    # Render Board
    def render(self):
        matrix = self.board_matrix()
        for row in matrix:
            print(row)


def main():
    game = Game(10, 20)
    # print(game)
    game.render()

if __name__ == "__main__":
    main()