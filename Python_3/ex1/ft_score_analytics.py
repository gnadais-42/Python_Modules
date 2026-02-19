import sys


def main() -> None:
    arguments: list = sys.argv
    if len(arguments) == 1:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
        sys.exit()
    scores: list = []
    for i in range(1, len(arguments)):
        try:
            scores.append(int(arguments[i]))
        except ValueError:
            pass
    if len(scores) == 0:
        print("Please provide valid scores")
        sys.exit()
    print(f"Scores processed: {scores}\n"
          f"Total players: {len(scores)}\n"
          f"Average score: {sum(scores) / len(scores)}\n"
          f"High score: {max(scores)}\n"
          f"Low score: {min(scores)}\n"
          f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
