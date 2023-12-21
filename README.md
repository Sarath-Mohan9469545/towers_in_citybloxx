# Towers in City Bloxx
Analysis of tower placement in the game City Bloxx

In the mobile game City Bloxx, there are towers of four different colors (blue, red, green and yellow) that can be built to progress in the game. Each colored tower has value associated with it, with blue having the lowest value and yellow having the highest. The towers are build in an nxn sized grid, with each tower taking a single suqare in the gird.

There are certain rules that need to be followed when building these towers:
    1. To build an yellow tower in a square, there needs to be a red, a blue, and a green tower on any of the 4 adjacent neighbours of the square.
    2. To build a green tower in a square, there needs to be a red, and a blue tower on any of the 4 adjacent neighbours of the square.
    3. To build a red tower in a square, there needs to be a blue tower on any of the 4 adjacent neighbours of the square.

 The goal of the game is to achieve the maximum score by building the towers in the most efficient way possible.

 ## Initialization
This repoitory was tested in Python 3.11.7

 1. Clone the repostiory
 2. install the requirements from the requirements file in the towers_in_citybloxx folder: pip install -r requirements.txt

 ### Use Case 1 - Brute force method of obtaining a possible relatively high score city

 Use case 1 deals with giving a randomly generated city that follows the tower building criteria. You can specify the size of the city and the number of random generations created to find the highest scored city.

 Steps of the algorithm:
 1. Mention the city_size and num_iterations.
 2. Randomly generate a city of size city_sizeXcity_size.
 3. Check all squares of the city and find squares that do not follow the tower building criteria.
 4. Replace the towers in the faulty squares with the color that is the next lowest in value (b<r<g<y).
 5. Repeat steps 3 and 4 until the city is completely faultless.
 6. Repeat the steps 2 to 5 for num_iterations and return the city that has the highest score.

Run the brute_force.py script to produce the city.

 cd towers_in_citybloxx\towers_in_citybloxx\use_cases\use_case_1
 python brute_force.py <city_size> <num_iterations>


 ![Example of a city of size 5](towers_in_citybloxx\images\example_citysize_5.png)

 If not explicitily mentioned, the default values for city_size is 5 and num iterations is 10000.
 (City size should always be greater than 2).

