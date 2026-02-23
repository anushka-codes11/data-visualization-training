# Sample list of ratings (1-5), with some invalid entries
ratings = [5, 4, 3, 6, 2, 5, 0, 1, 5, 7]

# Step 1: Remove invalid ratings (keep only 1-5)
valid_ratings = [r for r in ratings if 1 <= r <= 5]

# Step 2: Calculate average rating
average_rating = sum(valid_ratings) / len(valid_ratings) if valid_ratings else 0

# Step 3: Count number of 5-star ratings
five_star_count = valid_ratings.count(5)

# Step 4: Sort ratings in ascending order
sorted_ratings = sorted(valid_ratings)

print("Valid Ratings:", valid_ratings)
print("Average Rating:", round(average_rating, 2))
print("Number of 5-star ratings:", five_star_count)
print("Ratings Sorted in Ascending Order:", sorted_ratings)