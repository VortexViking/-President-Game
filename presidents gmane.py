import random

# List of U.S. Presidents with their birth years, wife's first name, and whether they had a beard
presidents = [
    {"name": "george washington", "birth_year": 1732, "wife": "martha", "has_beard": False},
    {"name": "john adams", "birth_year": 1735, "wife": "abigail", "has_beard": False},
    {"name": "thomas jefferson", "birth_year": 1743, "wife": "martha", "has_beard": False},
    {"name": "james madison", "birth_year": 1751, "wife": "dolley", "has_beard": False},
    {"name": "james monroe", "birth_year": 1758, "wife": "elizabeth", "has_beard": False},
    {"name": "john quincy adams", "birth_year": 1767, "wife": "louisa", "has_beard": False},
    {"name": "andrew jackson", "birth_year": 1767, "wife": "rachel", "has_beard": False},
    {"name": "martin van buren", "birth_year": 1782, "wife": "hannah", "has_beard": False},
    {"name": "william henry harrison", "birth_year": 1773, "wife": "anna", "has_beard": False},
    {"name": "john tyler", "birth_year": 1790, "wife": "letitia", "has_beard": False},
    {"name": "james k. polk", "birth_year": 1795, "wife": "sarah", "has_beard": False},
    {"name": "zachary taylor", "birth_year": 1784, "wife": "margaret", "has_beard": False},
    {"name": "millard fillmore", "birth_year": 1800, "wife": "abigail", "has_beard": False},
    {"name": "franklin pierce", "birth_year": 1804, "wife": "jane", "has_beard": False},
    {"name": "james buchanan", "birth_year": 1791, "wife": "none", "has_beard": False},
    {"name": "abraham lincoln", "birth_year": 1809, "wife": "mary", "has_beard": True},
    {"name": "andrew johnson", "birth_year": 1808, "wife": "eliza", "has_beard": False},
    {"name": "ulysses s. grant", "birth_year": 1822, "wife": "julia", "has_beard": True},
    {"name": "rutherford b. hayes", "birth_year": 1822, "wife": "lucy", "has_beard": True},
    {"name": "james a. garfield", "birth_year": 1831, "wife": "lucretia", "has_beard": True},
    {"name": "chester a. arthur", "birth_year": 1829, "wife": "ellen", "has_beard": True},
    {"name": "grover cleveland", "birth_year": 1837, "wife": "frances", "has_beard": False},
    {"name": "benjamin harrison", "birth_year": 1833, "wife": "caroline", "has_beard": True},
    {"name": "william mckinley", "birth_year": 1843, "wife": "ida", "has_beard": False},
    {"name": "theodore roosevelt", "birth_year": 1858, "wife": "edith", "has_beard": False},
    {"name": "william howard taft", "birth_year": 1857, "wife": "helen", "has_beard": False},
    {"name": "woodrow wilson", "birth_year": 1856, "wife": "ellen", "has_beard": False},
    {"name": "warren g. harding", "birth_year": 1865, "wife": "florence", "has_beard": False},
    {"name": "calvin coolidge", "birth_year": 1872, "wife": "grace", "has_beard": False},
    {"name": "herbert hoover", "birth_year": 1874, "wife": "lou", "has_beard": False},
    {"name": "franklin d. roosevelt", "birth_year": 1882, "wife": "eleanor", "has_beard": False},
    {"name": "harry s. truman", "birth_year": 1884, "wife": "bess", "has_beard": False},
    {"name": "dwight d. eisenhower", "birth_year": 1890, "wife": "mamie", "has_beard": False},
    {"name": "john f. kennedy", "birth_year": 1917, "wife": "jacqueline", "has_beard": False},
    {"name": "lyndon b. johnson", "birth_year": 1908, "wife": "claudia", "has_beard": False},
    {"name": "richard nixon", "birth_year": 1913, "wife": "pat", "has_beard": False},
    {"name": "gerald ford", "birth_year": 1913, "wife": "betty", "has_beard": False},
    {"name": "jimmy carter", "birth_year": 1924, "wife": "rosalynn", "has_beard": False},
    {"name": "ronald reagan", "birth_year": 1911, "wife": "nancy", "has_beard": False},
    {"name": "george h. w. bush", "birth_year": 1924, "wife": "barbara", "has_beard": False},
    {"name": "bill clinton", "birth_year": 1946, "wife": "hillary", "has_beard": False},
    {"name": "george w. bush", "birth_year": 1946, "wife": "laura", "has_beard": False},
    {"name": "barack obama", "birth_year": 1961, "wife": "michelle", "has_beard": False},
    {"name": "donald trump", "birth_year": 1946, "wife": "melania", "has_beard": False},
    {"name": "joe biden", "birth_year": 1942, "wife": "jill", "has_beard": False}
]

def guessing_game():
    # Randomly choose a president
    chosen_president = random.choice(presidents)
    
    print("Welcome to the U.S. President Guessing Game!")
    print("I'm thinking of a U.S. president. Can you guess who it is?")
    print(f"Hint 1: The president was born in {chosen_president['birth_year']}.")
    print(f"Hint 2: The president's wife's first name is {chosen_president['wife']}.")
    print(f"Hint 3: The president {'had' if chosen_president['has_beard'] else 'did not have'} a beard.")
    
    score = 0
    attempts = 0
    max_attempts = 5
    guessed_correctly = False
    
    while attempts < max_attempts and not guessed_correctly:
        guess = input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: ").strip().lower()  # Convert input to lowercase

        if guess not in [pres["name"] for pres in presidents]:
            print("That is not a valid president's name. Try again.")
            continue

        attempts += 1

        if guess == chosen_president["name"]:
            if attempts == 1:
                score += 2  # 2 points if guessed on the first try
                print(f"Correct! You guessed it on the first try. You get 2 points.")
            else:
                score += 1  # 1 point if guessed correctly on other attempts
                print(f"Correct! You get 1 point.")
            guessed_correctly = True
        elif guess < chosen_president["name"]:
            print("Guess higher!")
            score -= 1  # Deduct 1 point for an incorrect guess
        elif guess > chosen_president["name"]:
            print("Guess lower!")
            score -= 1  # Deduct 1 point for an incorrect guess

    if not guessed_correctly:
        print(f"Sorry, you've used all {max_attempts} attempts. The correct answer was {chosen_president['name']}.")
    
    print(f"Game over! Your total score is: {score}")

# Start the game
guessing_game()
