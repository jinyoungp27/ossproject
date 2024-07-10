
### 1. Related works

https://github.com/ankitjosh78/hang-movie-man
 - This is python-based hangman game played in the terminal. The game focuses on movie titles, and you can choose the language to play in before starting the game.

https://www.mycompiler.io/view/6OyzAKLGJ5a
 - This is a simple spelling game played on the web based on Python. It takes an alphabet letter input from the user and then checks whether the entered letter is included in the word.

https://github.com/timmyjose-projects/hangman
- This is a simple hangman game played in the terminal based on Python. The user can specify the difficulty in detail at the beginning, including the word length and the number of attempts. The game is won if the word is gussed within the specified number of attempts.


### 2. Proposals
Feeling the need for UI design for user convenience, we decided to make Python-based basic hangman and use pygame. In order for the game to proceed smoothly, it will be divided into three stages: easy, noraml, and hard rather than free input by users. And developed the code by deleting alphabets that are not included in words when users find it difficult to proceed with the game.