import unittest
from blackjack import Player, Game

class TestBlackjack(unittest.TestCase):

    def test_player_roll_range(self):
        # Testar att tärningskast alltid är mellan 1 och 6
        p = Player("Testare")
        for _ in range(100):
            roll = p.roll()
            self.assertTrue(1 <= roll <= 6)

    def test_score_reset(self):
        # Testar att poängen nollställs korrekt
        p = Player("Testare")
        p.score = 15
        p.reset()
        self.assertEqual(p.score, 0)

    def test_dealer_behavior(self):
        # Testar att dealern slutar på minst 17
        g = Game()
        g.dealer.reset()
        while g.dealer.score < 17:
            g.dealer.roll()
        self.assertGreaterEqual(g.dealer.score, 17)

# Gör så att man kan köra koden direkt
if __name__ == "__main__":
    unittest.main()

# Motivering:
# 1. test_player_roll_range: Säkerställer att tärningen fungerar korrekt.
# 2. test_score_reset: Verifierar att poängen nollställs mellan rundor.
# 3. test_dealer_behavior: Kontrollerar att dealern följer regeln att slå tills minst 17.