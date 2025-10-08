from engi.core.brain import ENGI

if __name__ == "__main__":
    engi = ENGI()
    print("💜 ENGI is online. Say 'hi', 'stress', 'efficiency' or 'pid'.")
    try:
        while True:
            user = input("You: ")
            print("ENGI:", engi.think(user))
    except (KeyboardInterrupt, EOFError):
        print("\nENGI: Bye, engineer 💜")
