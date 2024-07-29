def evaluate_guess(guess, model):

    well_placed = 0
    misplaced = 0

    model_count = {}
    guess_count = {}

    # First pass: count well placed pegs
    for i in range(len(model)):
        if guess[i] == model[i]:
            well_placed += 1
        else:
            # Count colors in model and guess for misplaced calculation
            model_count[model[i]] = model_count.get(model[i], 0) + 1
            guess_count[guess[i]] = guess_count.get(guess[i], 0) + 1

    # Second pass: count misplaced pegs
    for color in guess_count:
        if color in model_count:
            misplaced += min(model_count[color], guess_count[color])

    return well_placed, misplaced


# Model and next guess
model = ["R", "G", "B", "Y"]
next_guess = ["G", "R", "B", "B"]

# Evaluate the next guess
well_placed, misplaced = evaluate_guess(next_guess, model)

# Print the results
print(f"Well placed: {well_placed}, Misplaced: {misplaced}")

