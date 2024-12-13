CREATE TABLE Fitnessapp (
    "workout_name" TEXT NOT NULL,
    "number_weight" INTEGER CHECK(number_weight >= 0),
    "number_sets" INTEGER  CHECK(number_sets >= 0),
    "number_reps" INTEGER CHECK(number_reps >= 0),
    "rest_secs" INTEGER CHECK(rest_secs >= 0),
    PRIMARY KEY("workout_name")
	);
	
INSERT INTO Fitnessapp (workout_name, number_weight, number_sets, number_reps, rest_secs) 
VALUES ('Push-ups', ?, ?, ?, ?);

INSERT INTO Fitnessapp (workout_name, number_weight, number_sets, number_reps, rest_secs) 
VALUES ('Deadlifts', ?, ?, ?, ?);

INSERT INTO Fitnessapp (workout_name, number_weight, number_sets, number_reps, rest_secs) 
VALUES ('Squats', ?, ?, ?, ?);

INSERT INTO Fitnessapp (workout_name, number_weight, number_sets, number_reps, rest_secs) 
VALUES ('Leg Press', ?, ?, ?, ?);

INSERT INTO Fitnessapp (workout_name, number_weight, number_sets, number_reps, rest_secs) 
VALUES ('Hyperextention', ?, ?, ?, ?);	

INSERT INTO Fitnessapp (workout_name, number_weight, number_sets, number_reps, rest_secs) 
VALUES ('Hip Abduction', ?, ?, ?, ?)
	