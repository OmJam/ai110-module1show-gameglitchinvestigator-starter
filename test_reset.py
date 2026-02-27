"""
Tests for the new game reset fix.

Bug: clicking "New Game" only reset `attempts` and `secret`, leaving
`status`, `score`, and `history` from the previous game. If status was
"lost" or "won", the game was permanently blocked.

Fix: the reset now also clears status → "playing", score → 0, history → [].
"""


def make_end_state(status="lost"):
    """Return a session-state dict representing a finished game."""
    return {
        "attempts": 8,
        "secret": 42,
        "score": 75,
        "status": status,
        "history": [10, 20, 30, 40, 50, 60, 70, 80],
    }


def apply_old_reset(session, low=1, high=100):
    """Simulates the broken reset (only attempts + secret)."""
    import random
    session["attempts"] = 0
    session["secret"] = random.randint(low, high)
    return session


def apply_fixed_reset(session, low=1, high=100):
    """Simulates the corrected reset (all fields)."""
    import random
    session["attempts"] = 0
    session["secret"] = random.randint(low, high)
    session["status"] = "playing"
    session["score"] = 0
    session["history"] = []
    return session


# ---------------------------------------------------------------------------
# Tests that expose the old broken behaviour
# ---------------------------------------------------------------------------

def test_old_reset_leaves_status_blocked_after_loss():
    session = make_end_state(status="lost")
    apply_old_reset(session)
    # Old reset never touched status — game stays permanently blocked
    assert session["status"] == "lost"


def test_old_reset_leaves_status_blocked_after_win():
    session = make_end_state(status="won")
    apply_old_reset(session)
    assert session["status"] == "won"


def test_old_reset_leaves_stale_score():
    session = make_end_state()
    apply_old_reset(session)
    assert session["score"] == 75  # score carried over — not 0


def test_old_reset_leaves_stale_history():
    session = make_end_state()
    apply_old_reset(session)
    assert len(session["history"]) == 8  # history still full


# ---------------------------------------------------------------------------
# Tests that confirm the fixed reset works correctly
# ---------------------------------------------------------------------------

def test_fixed_reset_restores_status_to_playing_after_loss():
    session = make_end_state(status="lost")
    apply_fixed_reset(session)
    assert session["status"] == "playing"


def test_fixed_reset_restores_status_to_playing_after_win():
    session = make_end_state(status="won")
    apply_fixed_reset(session)
    assert session["status"] == "playing"


def test_fixed_reset_clears_score():
    session = make_end_state()
    apply_fixed_reset(session)
    assert session["score"] == 0


def test_fixed_reset_clears_history():
    session = make_end_state()
    apply_fixed_reset(session)
    assert session["history"] == []


def test_fixed_reset_clears_attempts():
    session = make_end_state()
    apply_fixed_reset(session)
    assert session["attempts"] == 0


def test_fixed_reset_respects_difficulty_range():
    """Secret should land within the provided low/high range."""
    for _ in range(50):
        session = make_end_state()
        apply_fixed_reset(session, low=1, high=20)   # Easy range
        assert 1 <= session["secret"] <= 20


def test_fixed_reset_allows_new_play():
    """After a fixed reset the game-blocking condition is gone."""
    session = make_end_state(status="lost")
    apply_fixed_reset(session)
    # The guard `if session["status"] != "playing": stop()` would NOT fire
    assert session["status"] == "playing"
    assert session["attempts"] == 0
    assert session["score"] == 0
    assert session["history"] == []
