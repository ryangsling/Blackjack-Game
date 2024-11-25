# Blackjack Game

## Overview
The **Blackjack Game** project is a Python implementation of the classic casino card game, Blackjack. It is an interactive, text-based game where the player competes against a computer dealer to get a hand closest to 21 without exceeding it.

---

## Features
- **Dynamic Card Dealing**: Simulates the randomness of card dealing.
- **Score Calculation**: Handles special rules, such as treating an Ace (`11`) as `1` if the total score exceeds `21`.
- **User Choices**: Allows the user to hit (draw a card) or stand (end their turn).
- **Dealer Logic**: The computer dealer automatically plays until reaching a score of `17` or higher.
- **Blackjack Check**: Automatically checks for Blackjack (score of `21` with two cards).
- **Interactive Feedback**: Provides real-time updates on scores and outcomes.
- **Replay Option**: Offers the player the option to replay the game after each round.

---

## Requirements
- **Python 3.x**: Ensure you have Python installed on your system.
- No additional libraries are required.

---

## How to Play
1. Clone or download this repository to your local machine.
2. Open the project in your preferred Python IDE or text editor.
3. Run the script in a terminal or IDE.
4. Follow the on-screen prompts to play.

### Gameplay Instructions
- Upon starting the game, you will receive two cards, and the dealer will also receive two cards (one hidden).
- You can choose to:
  - **Hit**: Draw another card to try to improve your score.
  - **Stand**: End your turn and let the dealer play.
- The game ends when:
  - Either player exceeds a score of `21` (bust).
  - The player or dealer gets a Blackjack.
  - Both players stand, and scores are compared.
- The game announces the winner based on the rules of Blackjack.

---

## Example Gameplay
```
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      `------'                           |__/                

	Your cards: [10, 7], current score: 17
	Computer's first card: 8

	Type hit to pick another card, otherwise type stand.
stand

	Your final hand: [10, 7], final score: 17
	Computer's final hand: [8, 10], final score: 18

	You lose!
```

---

## Code Explanation
### Key Functions
1. **`deal_card()`**:
   - Returns a random card from a standard deck.
2. **`calculate_score(cards)`**:
   - Calculates the total score of a hand, with special handling for Aces.
   - Returns `0` for a Blackjack.
3. **`compare(user_score, computer_score)`**:
   - Compares the player's and dealer's scores to determine the winner.
4. **`play_game()`**:
   - Core function to handle the game flow, including user and dealer turns.

---

## Contributing
If you'd like to contribute to this project:
1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.

---

## Acknowledgments
- Inspired by the classic Blackjack card game.
- ASCII art generated to enhance the visual appeal of the game.

