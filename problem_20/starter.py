"""
CodingQuest Problem 20: Tic tac toe

Your input data is in input.txt.
The data has been loaded into a list called `data` for you.
Each item in the list is one line from the file, as a string.

Each line represents one game of tic-tac-toe.
The numbers on each line are the squares played, in order (X goes first).
Squares are numbered like this:

 1 | 2 | 3
---|---|---
 4 | 5 | 6
---|---|---
 7 | 8 | 9

Process each game until someone wins (3 in a row), then stop.
If nobody wins after 9 moves, it's a draw.

Your answer is: (games won by X) * (games won by O) * (drawn games)

Write your solution below the comment line.
"""

# --- Your code here ---
def process_ship_ai_games(data):
    
    winning_combinations = [
        {1, 2, 3}, {4, 5, 6}, {7, 8, 9},  # Rows
        {1, 4, 7}, {2, 5, 8}, {3, 6, 9},  # Columns
        {1, 5, 9}, {3, 5, 7}              # Diagonals
    ]
    
    wins_x = 0
    wins_o = 0
    draws = 0
    
    
    lines = data
    
    for line in lines:
        moves = list(map(int, line.split()))
        x_moves = set()
        o_moves = set()
        game_resolved = False
        
        for i, move in enumerate(moves):
            
            if i % 2 == 0:
                x_moves.add(move)
                current_player_moves = x_moves
                current_player_label = 'X'
            else:
                o_moves.add(move)
                current_player_moves = o_moves
                current_player_label = 'O'
            
            
            for combo in winning_combinations:
                if combo.issubset(current_player_moves):
                    if current_player_label == 'X':
                        wins_x += 1
                    else:
                        wins_o += 1
                    game_resolved = True
                    break
            
            
            if game_resolved:
                break
        
        
        if not game_resolved:
            draws += 1

    
    total_value = wins_x * wins_o * draws
    
    return {
        "X Wins": wins_x,
        "O Wins": wins_o,
        "Draws": draws,
        "Final Value": total_value
    }




# --- Load the data (don't change this) ---
with open("input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]
    print(process_ship_ai_games(data))


