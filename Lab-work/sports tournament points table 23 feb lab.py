# Sample list of team points
points = [25, 30, -5, 18, 40, 22, -2]

# Step 1: Replace negative points with 0
points = [p if p >= 0 else 0 for p in points]

# Step 2: Sort leaderboard in descending order
sorted_points = sorted(points, reverse=True)

# Step 3: Find winner and runner-up
winner = sorted_points[0] if sorted_points else None
runner_up = sorted_points[1] if len(sorted_points) > 1 else None

print("Leaderboard (sorted):", sorted_points)
print("Winner (highest points):", winner)
print("Runner-up (second highest points):", runner_up)