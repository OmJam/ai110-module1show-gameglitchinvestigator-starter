from logic_utils import check_guess

# ── outcome tests ──────────────────────────────────────────────────────────────

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

# ── message tests (catches the swapped-hint bug) ───────────────────────────────

def test_too_high_message_says_go_lower():
    # Bug: when guess > secret the message incorrectly said "Go HIGHER!"
    # The correct hint when you've guessed too high is to go LOWER.
    _, message = check_guess(60, 50)
    assert "LOWER" in message, f"Expected hint to say LOWER, got: {message!r}"

def test_too_low_message_says_go_higher():
    # Bug: when guess < secret the message incorrectly said "Go LOWER!"
    # The correct hint when you've guessed too low is to go HIGHER.
    _, message = check_guess(40, 50)
    assert "HIGHER" in message, f"Expected hint to say HIGHER, got: {message!r}"

def test_too_high_message_does_not_say_go_higher():
    # Explicit negative check: "Go HIGHER!" must NOT appear when guess is too high
    _, message = check_guess(99, 1)
    assert "HIGHER" not in message, f"Hint wrongly said HIGHER when guess was too high: {message!r}"

def test_too_low_message_does_not_say_go_lower():
    # Explicit negative check: "Go LOWER!" must NOT appear when guess is too low
    _, message = check_guess(1, 99)
    assert "LOWER" not in message, f"Hint wrongly said LOWER when guess was too low: {message!r}"

def test_win_returns_two_values():
    result = check_guess(42, 42)
    assert len(result) == 2

def test_non_win_returns_two_values():
    result = check_guess(10, 50)
    assert len(result) == 2
