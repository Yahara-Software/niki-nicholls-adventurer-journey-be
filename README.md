# Adventurer Journey - Back End
Please complete the story below and create a program to solve the problem. Commit any work back to the remote no later than 48 hours before the next interview.

*Please use whatever languages, references and tooling you would like to complete the story.*

## Story Instructions
You are an adventurer standing in the center of a map facing North, and you’re trying to weave through the terrain to your final destination. You have the directions to your destination indicating the number of steps and the direction to travel.

Adventurer Path & Instructions - [./Adventurer Path.md](./Adventurer%20Path.md)

Given the Path Instructions above, programmatically parse the instructions and determine what is the Euclidean (straight line) distance from your starting point to the destination in steps?

**Tech Notes:**
- Use whatever languages, references and tooling you would like.
- Provide any needed instructions to run program.
- Do not round to the nearest step.
- After program executes the answer should be returned.

**To Run the Program:**
- Run main.py
- Program automatically tests instructions "15F6B6B5L16R8B16F20L6F13F11R" then allows the user to enter new instructions if desired
- To run test cases run distance_calculator_tests.py
- Program uses Python 3.12

**NOTE:**
The program has two methods to calculate euclidean distance:

1. One method assumes that the adventurer is always facing North. For example "5R5R" translates to 5 steps East, 5 steps East.
2. The other method assumes that the adventurer changes the direction they are facing with each instruction. For example "5R5R" translates to 5 steps East, 5 Steps South. This is because after the adventurer follows the first instruction "5R" they are now facing East and the next instruction "5R" will direct them 5 steps South. 

