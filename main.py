from distance_calculator import DistanceCalculator

calculator = DistanceCalculator()

instructions = "15F6B6B5L16R8B16F20L6F13F11R"
print(f"Instructions: {instructions}")
print(f"Euclidean Distance where F == N, B == S, R == E, L == W: "
      f"{calculator.calculate_fixed_direction_distance(instructions)} steps")
print(f"Euclidean Distance where instructions are relative to the direction the person is facing: "
      f"{calculator.calculate_relative_direction_distance(instructions)} steps")

while True:
    user_input = input("\nEnter new instructions or 'Q' to quit: ")
    if user_input.upper() == 'Q':
        break
    print(f"Euclidean Distance where F == N, B == S, R == E, L == W: "
          f"{calculator.calculate_fixed_direction_distance(user_input)} steps")
    print(f"Euclidean Distance where instructions are relative to the direction the person is facing: "
          f"{calculator.calculate_relative_direction_distance(user_input)} steps")
