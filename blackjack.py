import random

# Klass för spelare
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def roll(self):
        value = random.randint(1, 6)
        self.score += value
        return value

    def reset(self):
        self.score = 0

# Klass för spelet
class Game:
    def __init__(self):
        self.player = Player("Spelare")
        self.dealer = Player("Dealer")
        self.player_wins = 0
        self.dealer_wins = 0
        self.load_highscore()

    def load_highscore(self):
        try:
            with open("highscore.txt", "r") as f:
                lines = f.read().split(",")
                self.player_wins = int(lines[0])
                self.dealer_wins = int(lines[1])
        except FileNotFoundError:
            self.player_wins = 0
            self.dealer_wins = 0

    def save_highscore(self):
        # Sparar highscore till fil
        with open("highscore.txt", "w") as f:
            f.write(f"{self.player_wins},{self.dealer_wins}")

    def play_round(self):
        self.player.reset()
        self.dealer.reset()

        # Spelarens tur
        while True:
            print(f"\n{self.player.name} poäng: {self.player.score}")
            choice = input("Vill du rulla (r) eller stanna (s)? ").lower()
            if choice == "r":
                roll = self.player.roll()
                print(f"Du rullade: {roll}")
                if self.player.score > 21:
                    print("Du fick över 21! Du förlorar.")
                    self.dealer_wins += 1
                    self.save_highscore()
                    return
            elif choice == "s":
                print(f"Du stannar på {self.player.score}")
                break
            else:
                print("Ogiltigt val. Skriv 'r' eller 's'.")

        # Dealerns tur
        while self.dealer.score < 17:
            roll = self.dealer.roll()
            print(f"Dealern rullade: {roll} (total: {self.dealer.score})")

        # Avgör vinnare
        print(f"\nSlutresultat:\nSpelare: {self.player.score}\nDealer: {self.dealer.score}")
        if self.dealer.score > 21 or self.player.score > self.dealer.score:
            print("Du vinner!")
            self.player_wins += 1
        elif self.player.score < self.dealer.score:
            print("Du förlorar.")
            self.dealer_wins += 1
        else:
            print("Oavgjort!")

        self.save_highscore()

    def show_score(self):
        print(f"\nStällning: Spelare {self.player_wins} - Dealer {self.dealer_wins}")

# Startar spelet
def main():
    game = Game()
    print("Välkommen till NotBlackjack!")
    while True:
        game.play_round()
        game.show_score()
        again = input("\nVill du spela igen? (j/n): ").lower()
        if again != "j":
            print("Tack för att du spelade!")
            break

if __name__ == "__main__":
    main()