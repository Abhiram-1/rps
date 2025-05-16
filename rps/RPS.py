def player(prev_play, opponent_history=[]):
    # Initialize the move counter if it doesn't exist
    if "move_counter" not in player.__dict__:
        player.move_counter = 0
        player.my_history = []
        player.opponent_history = []
        player.potential_patterns = {}
        player.pattern_length = 10
        player.counter_moves = {"R": "P", "P": "S", "S": "R"}
        player.ideal_response = {'R': 'P', 'P': 'S', 'S': 'R'}
        player.moves = ["R", "P", "S"]
        player.move_freq = {"R": 0, "P": 0, "S": 0}
    
    # First move strategy - start with paper (beats rock)
    if prev_play == "":
        player.move_counter = 0
        player.my_history = []
        player.opponent_history = []
        player.potential_patterns = {}
        player.move_freq = {"R": 0, "P": 0, "S": 0}
        return "P"
    
    # Update histories
    player.opponent_history.append(prev_play)
    player.move_counter += 1
    
    # Update frequency analysis
    player.move_freq[prev_play] += 1
    
    # Pattern recognition - look for sequences in opponent's play
    if player.move_counter > player.pattern_length:
        # Look at the last n moves
        last_n = "".join(player.opponent_history[-(player.pattern_length):])
        
        # Check if we've seen this pattern before
        if last_n in player.potential_patterns:
            player.potential_patterns[last_n] += 1
        else:
            player.potential_patterns[last_n] = 1
    
    # Make a prediction based on pattern matching
    prediction = ""
    highest_conf = 0
    
    # If we have enough history, try to match patterns
    if player.move_counter >= player.pattern_length:
        recent_pattern = "".join(player.opponent_history[-(player.pattern_length-1):])
        
        # Look for matching patterns and their next moves
        for pattern, freq in player.potential_patterns.items():
            if pattern.startswith(recent_pattern) and freq > highest_conf:
                prediction = pattern[-1]  # Predict the last move of the pattern
                highest_conf = freq
    
    # If we found a predicted move with confidence
    if prediction and highest_conf > 2:
        counter_move = player.counter_moves[prediction]
    else:
        # Fallback to frequency analysis to counter most common move
        total_moves = sum(player.move_freq.values())
        if total_moves > 0:
            # Find the most frequent move
            most_frequent = max(player.move_freq, key=player.move_freq.get)
            counter_move = player.counter_moves[most_frequent]
        else:
            # If no moves yet, default to paper
            counter_move = "P"
    
    # Store my move for next iteration
    player.my_history.append(counter_move)
    
    return counter_move