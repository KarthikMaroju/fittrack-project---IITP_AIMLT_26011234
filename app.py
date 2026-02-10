def add_workout(workouts, workout):
    workouts.append(workout)
    return workouts

workout_list = []

while True:
    workout = input("Enter workout (or type exit): ")
    if workout.lower() == "exit":
        break
    add_workout(workout_list, workout)

print("Your Workouts:")
for w in workout_list:
    print("-", w)

