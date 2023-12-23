import tkinter as tk
import random

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.canvas = tk.Canvas(self.master, width=400, height=400, bg='black')
        self.canvas.pack()
        self.master.bind('<KeyPress>', self.change_direction)

        self.snake = [(200, 200), (210, 200), (220, 200)]
        self.food = self.create_food()
        self.direction = 'Left'
        self.game_over = False
        self.update_delay = 100

        self.move_snake()

    def create_food(self):
        while True:
            x = random.randrange(10, 390, 10)
            y = random.randrange(10, 390, 10)
            if (x, y) not in self.snake:
                return x, y

    def draw_snake(self):
        self.canvas.delete('snake')
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0]+10, segment[1]+10,
                                         fill='green', outline='black', tags='snake')

    def draw_food(self):
        self.canvas.delete('food')
        self.canvas.create_oval(self.food[0], self.food[1], self.food[0]+10, self.food[1]+10,
                                fill='red', outline='black', tags='food')

    def move_snake(self):
        head = dict()
        head['Left'] = (-10, 0)
        head['Right'] = (10, 0)
        head['Up'] = (0, -10)
        head['Down'] = (0, 10)

        if not self.game_over:
            new_head = (self.snake[0][0] + head[self.direction][0], self.snake[0][1] + head[self.direction][1])

            if new_head[0] < 0 or new_head[0] >= 400 or new_head[1] < 0 or new_head[1] >= 400 or new_head in self.snake:
                self.game_over = True

            self.snake.insert(0, new_head)

            if self.snake[0] == self.food:
                self.food = self.create_food()
            else:
                self.snake.pop()

            self.draw_snake()
            self.draw_food()

            if not self.game_over:
                self.master.after(self.update_delay, self.move_snake)
            else:
                self.canvas.create_text(200, 200, text="Game Over!", fill='white', font=('Arial', 24))

    def change_direction(self, event):
        if event.keysym in ['Left', 'Right', 'Up', 'Down']:
            if (event.keysym == 'Left' and self.direction != 'Right') or \
               (event.keysym == 'Right' and self.direction != 'Left') or \
               (event.keysym == 'Up' and self.direction != 'Down') or \
               (event.keysym == 'Down' and self.direction != 'Up'):
                self.direction = event.keysym

def main():
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()