
### 1. Related works

https://github.com/ankitjosh78/hang-movie-man<br>
 - console 창에서 진행하는 hangman게임, 주제가 영화 제목으로만 이뤄져 있음, 게임할 언어 선택가능, 

https://www.mycompiler.io/view/6OyzAKLGJ5a
 - 사용자로부터 알파벳 하나를 입력받은 후, 예측한 글자가 단어에 포함되는지 판단하는 방식

https://github.com/timmyjose-projects/hangman
터미널에서 진행하는 행맨 게임, 사용자가 처음에 단어 길이와 시도할 횟수 등 난이도를 상세하게 지정할 수 있음, 지정한 횟수 안에 단어를 맞추면 이기고, 단어를 못맞추면 지는 게임


### 2. Proposals
게임 진행을 위한 UI 필요, 단어 주제의 다양화 필요 , 시도할 횟수 제한, 힌트 제공 필요
힌트의 방향 변경, 단어에 포함되지 않은 알파벳을 제거하는 방식으로 수정
