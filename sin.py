import numpy as np
import pygame

pygame.init()

# CONSTANTS
WIDTH, HEIGHT = 800, 800

def desired_function(x):
    return 0.3 * x + 0.2

def map_point(x, y):
        px = (x + 1) / 2 * WIDTH
        py = HEIGHT - (y + 1) / 2 * HEIGHT
        
        return px, py

class Point():
    def __init__(self):
        self.x = np.random.uniform(-1, 1) 
        self.y = np.random.uniform(-1, 1) 
        self.label = 1 if self.y > desired_function(self.x) else -1

    def show(self, screen, brain):
        if brain.activate([self.x, self.y]) == self.label:
            color = (0, 255, 0)
        else:
            color = (255, 0, 0)
        pygame.draw.circle(screen, color, map_point(self.x, self.y), 5)

class Perceptron():
    def __init__(self):
        # 2 weights plus 1 for the bias
        self.weights = np.random.uniform(-1, 1, 3)

    def activation(self, x):
        return 1 if x >= 0 else -1

    def activate(self, inputs):
        sum = np.dot(self.weights, [*inputs, 1])
        return self.activation(sum)
    
    def train(self, inputs, target, learning_rate):
        predicted = self.activate(inputs)
        error = target - predicted
        for i in range(2):
            self.weights[i] += error * inputs[i] * learning_rate
        self.weights[2] += error * learning_rate

    def guessY(self, x):
        return -(self.weights[2]/self.weights[1]) - (self.weights[0]/self.weights[1]) * x


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sin-NN")
clock = pygame.time.Clock()

def generate_dataset():
    points = []
    for _ in range(100):
        points.append(Point())
    return points

def show_line(screen, brain):
    pygame.draw.line(screen, (0, 0, 255), map_point(-1, desired_function(-1)), map_point(1, desired_function(1)))
    pygame.draw.line(screen, (255, 155, 0), map_point(-1, brain.guessY(-1)), map_point(1, brain.guessY(1)))

points = generate_dataset()

brain = Perceptron()

learning_rate = 0.01

# Main game loop
running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for pt in points:
                inputs = [pt.x, pt.y]
                brain.train(inputs, pt.label, learning_rate)

    for point in points:
        point.show(screen, brain)
    
    show_line(screen, brain)

    clock.tick(60)
    
    pygame.display.flip()
