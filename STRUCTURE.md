#brief structure of the program
breif description : 난이도에 따른 단어 길이와 틀릴 횟수에 차이를 둔 간단한 hangman game

1. 중점 기능 functions
- give_hint() : A function that checks whether a hint can be provided. The maximum number of hints is 3. Each time the "hint" button on the screen is pressed, the give_hint() functions is called, which eliminates one of the unselected letter and update the usage count.

- random_word() : This function selects a word randomly from a file based on the difficulty level chosen in the main_menu()

- main_menu() : This functions draws the start screen where the difficulty level can be selected. After selecting the difficulty level, it calls the random_word() function to transition to the game screen.

