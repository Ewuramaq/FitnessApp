class Exercise:
    def __init__(self, name, weight, reps, sets, rest_time):
        
        self.name = name
        self.weight = weight
        self.reps = reps
        self.sets = sets
        self.rest_time = rest_time

    def __str__(self):
       
        return (f"Exercise: {self.name}\n"
                f"Weight: {self.weight}\n"
                f"Reps: {self.reps}\n"
                f"Sets: {self.sets}\n"
                f"Rest Time: {self.rest_time} seconds\n")

def main():
    print("This is your workout planner!\n")
    
    # Prompt for user to create an exercise
    exercise_name = input("Enter the name of your exercise: ")
    weight = int(input(f"Enter the number of weight (in kg) for {exercise_name}: "))
    reps = int(input(f"Enter the number of reps for {exercise_name}: "))
    sets = int(input(f"Enter the number of sets for {exercise_name}: "))
    rest_time = int(input(f"Enter the rest time (in seconds) between sets for {exercise_name}: "))

    # Exercise object
    user_exercise = Exercise(name=exercise_name, weight=weight, reps=reps, sets=sets, rest_time=rest_time)
    
    print("\nHere is your workout:")
    print(user_exercise)
    
    for set_number in range(1, user_exercise.sets + 1):
        print(f"Set {set_number} of {user_exercise.sets}: Perform {user_exercise.reps} {user_exercise.name}.")
        if set_number < user_exercise.sets:
            print(f"Rest for {user_exercise.rest_time} seconds...")
    
    print("\nWorkout complete! Great job!")

if __name__ == "__main__":
    main()
