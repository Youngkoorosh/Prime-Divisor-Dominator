match_teams = [
    ("Iran", "Spain"),
    ("Iran", "Portugal"),
    ("Iran", "Morocco"),
    ("Spain", "Portugal"),
    ("Spain", "Morocco"),
    ("Portugal", "Morocco")
]

teams = {
    "Iran": {"points": 0, "wins": 0, "draws": 0, "goal difference": 0},
    "Spain": {"points": 0, "wins": 0, "draws": 0, "goal difference": 0},
    "Portugal": {"points": 0, "wins": 0, "draws": 0, "goal difference": 0},
    "Morocco": {"points": 0, "wins": 0, "draws": 0, "goal difference": 0}
}

matches = []

print("Enter scores for 6 matches (format: ScoreA-ScoreB):")
for team1, team2 in match_teams:
    line = input(f"{team1} vs {team2}: ")
    score1, score2 = map(int, line.strip().split("-"))
    matches.append((team1, score1, team2, score2))

# Process match results
for team1, score1, team2, score2 in matches:
    teams[team1]["goal difference"] += score1 - score2
    teams[team2]["goal difference"] += score2 - score1

    if score1 > score2:
        teams[team1]["points"] += 3
        teams[team1]["wins"] += 1
    elif score1 < score2:
        teams[team2]["points"] += 3
        teams[team2]["wins"] += 1
    else:
        teams[team1]["points"] += 1
        teams[team2]["points"] += 1
        teams[team1]["draws"] += 1
        teams[team2]["draws"] += 1

sorted_teams = sorted(
    teams.items(),
    key=lambda x: (-x[1]["points"], -x[1]["wins"], x[0])
)
  
for team, stats in sorted_teams:
    print(f"{team}  wins:{stats['wins']} , loses:{stats['loses']} , draws:{stats['draws']} , goal difference:{stats['goal difference']} , points:{stats['points']}")


            
