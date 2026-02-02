print("=== Game Analytics Dashboard ===\n")


players = ["alice", "bob", "charlie", "diana"]
scores = {
    "alice": 2300,
    "bob": 1800,
    "charlie": 2150,
    "diana": 1950,
}
achievements = {
    "alice": ["first_kill", "level_10", "boss_slayer",
              "speed_run", "collector"],
    "bob": ["first_kill", "level_10", "collector"],
    "charlie": ["first_kill", "level_10", "boss_slayer",
                "collector", "explorer", "veteran", "champion"],
    "diana": ["first_kill", "explorer"],
}
regions = {
    "alice": "north",
    "bob": "east",
    "charlie": "central",
    "diana": "north",
}
active_status = {
    "alice": True,
    "bob": True,
    "charlie": True,
    "diana": False,
}


print("=== List Comprehension Examples ===")

high_scorers = [p for p in players if scores[p] > 2000]
print("High scorers (>2000):", high_scorers)

scores_doubled = [scores[p] * 2 for p in players]
print("Scores doubled:", scores_doubled)

active_players = [p for p in players if active_status[p]]
print(f"Active players: {active_players}\n")


print("=== Dict Comprehension Examples ===")

player_scores = {p: scores[p] for p in players}
print("Player scores:", player_scores)

score_categories = {
    "high": len([p for p in players if scores[p] >= 2200]),
    "medium": len([p for p in players if 1800 <= scores[p] < 2200]),
    "low": len([p for p in players if scores[p] < 1800]),
}
print("Score categories:", score_categories)

achievement_counts = {p: len(achievements[p]) for p in players}
print(f"Achievement counts: {achievement_counts}\n")


print("=== Set Comprehension Examples ===")

unique_players = {p for p in players}
print("Unique players:", unique_players)

unique_achievements = {
    a
    for plist in achievements.values()
    for a in plist
}
print("Unique achievements:", unique_achievements)

active_regions = {
    regions[p]
    for p in players
    if active_status[p]
}
print(f"Active regions: {active_regions}\n")


print("=== Combined Analysis ===")

total_players = len(players)
print("Total players:", total_players)

total_unique_achievements = len(unique_achievements)
print("Total unique achievements:", total_unique_achievements)

average_score = sum(scores.values()) / len(scores)
print("Average score:", average_score)

top_player = max(scores, key=lambda p: scores[p])
print(
    "Top performer:",
    top_player,
    "(",
    scores[top_player],
    "points,",
    len(achievements[top_player]),
    "achievements)"
)
