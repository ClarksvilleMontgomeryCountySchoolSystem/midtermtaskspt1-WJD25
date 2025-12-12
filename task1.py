# TEST DATA - Do not modify
creator_name = "DigitalDreamer"
current_followers = 4567
starting_followers = 2100
days_tracked = 45
milestone_increment = 1000

# YOUR CODE BELOW THIS LINE
# Calculate follower statistics and milestone progress

# Calculate milestone progress
current_milestone =current_followers// milestone_increment
progress_in_milestone = current_followers%milestone_increment
total_gained = current_followers - starting_followers

# Calculate growth statistics
daily_average = total_gained//days_tracked

# Calculate projections
days_to_milestone = (milestone_increment - progress_in_milestone)//daily_average
weekly_growth = daily_average*7

# Display results with f-strings
print(f'Creator: {creator_name}\nCurrent Milestone: {current_milestone}\nProgress in Milestone: {progress_in_milestone} followers\ntotal Growth: {total_gained} followers\nDaily Average: {daily_average} followers\nDays to Next Milestone:{days_to_milestone} days\nWeekly Growth Projection: {weekly_growth} followers')
