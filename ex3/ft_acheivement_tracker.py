if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    Alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
    Bob = {"first_kill", "level_10", "boss_slayer", "collector"}
    Charlie = {"level_10", "treasure_hunter", "boss_slayer", "speed_demon", "perfectionist"}

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
