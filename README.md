# Turtle Crossing Game

This project is a simple game implemented in Python using the Turtle module. The objective of the game is to control a turtle crossing a busy road without colliding with oncoming cars. As the game progresses, the speed of the cars increases, making it more challenging for the player.

## How to Play
- Use the "Up" arrow key to move the turtle upwards, trying to reach the top of the screen without colliding with any cars.
- Each successful crossing increases the level and speeds up the cars, making the game more challenging.
- If the turtle collides with a car, the game ends, and the player receives a "GAME OVER" message.

## Usage
### Prerequisites
- Python 3.x

### Installation
1. Clone this repository to your local machine:
   
```bash
git clone https://github.com/alyssawalter/turtle-crossing-game.git
``` 
2. Navigate to the project directory:

```bash
cd turtle-crossing-game
```

### Running the Game
Run the main.py script:
```bash
python main.py
```

## File Structure
- main.py: Main script containing the game loop and initialization of game objects.
- player.py: Class definition for the player turtle and its movement.
- car_manager.py: Class definition for managing cars, their movement, and speed.
- scoreboard.py: Class definition for managing the game's scoreboard.
  
## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License
MIT License
