# README for Basic Perceptron Visualization

## Description

This Python script creates a visualization of a simple perceptron learning to approximate a linear function using the Pygame library. The perceptron will be trained interactively with the mouse click event and its learning will be reflected in real-time.

## Dependencies

- `numpy`
- `pygame`

To install these dependencies:

```
pip install numpy pygame
```

## How it Works

1. **Constants**:
    - `WIDTH, HEIGHT`: Dimensions of the pygame window.
  
2. **Function Definitions**:
    - `desired_function(x)`: Returns the y-value of the linear function for a given x-value.
    - `map_point(x, y)`: Maps a point in the range (-1,1) to pixel coordinates in the window.
  
3. **Classes**:
    - `Point`: Represents a random point with labels depending on its position relative to the desired function.
    - `Perceptron`: A simple perceptron with weights, an activation function, a function to predict labels for given inputs, and a training method.
  
4. **Pygame Setup**:
    - Initializes a window of size `WIDTH x HEIGHT` with the caption "Sin-NN".
  
5. **Main Loop**:
    - Displays the points and the desired function line.
    - On a mouse click, it trains the perceptron with the existing dataset.
    - Updates the perceptron's approximation of the line in real-time.

## Usage

1. Run the script.
2. A window will pop up displaying points colored either green or red. The blue line represents the desired function, while the orange line represents the perceptron's current approximation.
3. Click anywhere in the window to train the perceptron.
4. Observe the orange line adjust as the perceptron learns.
5. Close the window to end the program.
