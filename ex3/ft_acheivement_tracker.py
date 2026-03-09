if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    player_achievements = {
        "alice": [
            "first_blood",
            "pixel_perfect",
            "speed_runner",
            "first_blood",
            "first_blood"
        ],
        "bob": [
            "level_master",
            "boss_hunter",
            "treasure_seeker",
            "level_master",
            "level_master"
        ],
        "charlie": [
            "treasure_seeker",
            "boss_hunter",
            "combo_king",
            "first_blood",
            "boss_hunter",
            "first_blood",
            "boss_hunter",
            "first_blood"
        ],
        "diana": [
            "first_blood",
            "combo_king",
            "level_master",
            "treasure_seeker",
            "speed_runner",
            "combo_king",
            "combo_king",
            "level_master"
        ],
        "eve": [
            "level_master",
            "treasure_seeker",
            "first_blood",
            "treasure_seeker",
            "first_blood",
            "treasure_seeker"
        ],
        "frank": [
            "explorer",
            "boss_hunter",
            "first_blood",
            "explorer",
            "first_blood",
            "boss_hunter"
        ]
    }

    Alice = set(player_achievements['alice'])
    Bob = set(player_achievements['bob'])
    Charlie = set(player_achievements['charlie'])

    print(f"Player alice Achievements: {Alice}")
    print(f"Player bob Achievements: {Bob}")
    print(f"Player charlie Achievements: {Charlie}")

    print("\n=== Achievement Analytics ===")

    all_unique = Alice.union(Bob, Charlie)

    print(f"All unique achievements: {all_unique}")
    print(f"Total unique achievements: {len(all_unique)}\n")

    all_common = Alice.intersection(Bob, Charlie)
    print(f"Common to all players: {all_common}")

    unique_alice = Alice.difference(Bob, Charlie)
    unique_bob = Bob.difference(Alice, Charlie)
    unique_charlie = Charlie.difference(Alice, Bob)

    rare_achievements = unique_alice.union(unique_bob, unique_charlie)

    print(f"Rare achievements (1 player): {rare_achievements}")

    alice_bob_common = Alice.intersection(Bob)
    print(f"Alice vs Bob common: {alice_bob_common}")

    alice_vs_bob_unique = Alice.difference(Bob)
    print(f"Alice unique: {alice_vs_bob_unique}")

    bob_vs_alice_unique = Bob.difference(Alice)
    print(f"Bob unique: {bob_vs_alice_unique}")
