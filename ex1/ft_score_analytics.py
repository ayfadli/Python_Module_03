import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if (len(sys.argv) == 1):
        print("No scores provided. Usage:", end=" ")
        print("python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        scores = []
        try:
            for arg in sys.argv[1:]:
                scores.append(int(arg))
            print(f"Scores processed: {scores}")
            print(f"Total players: {len(scores)}")
            print(f"Total score: {sum(scores)}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {int(max(scores) - min(scores))}")
        except ValueError:
            print("Error: specific scores must be integers", end=" ")
            print(f"(e.g. 1000, not {arg}).")
