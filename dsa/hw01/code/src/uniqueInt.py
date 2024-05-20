def process_file(input_file_path, output_file_path):
    # Define the range for valid integers
    MIN_VALUE, MAX_VALUE = -1023, 1023
    RANGE_SIZE = MAX_VALUE - MIN_VALUE + 1

    # Initialize a Boolean array to track presence of integers
    presence = [False] * RANGE_SIZE

    # Open input file for reading
    with open(input_file_path, 'r') as input_file:
        # Iterate through each line in the input file
        for line in input_file:
            stripped_line = line.strip()
            if stripped_line.startswith('-') and stripped_line[1:].isdigit() or stripped_line.isdigit():
                number = int(stripped_line)
                if MIN_VALUE <= number <= MAX_VALUE:
                    presence[number - MIN_VALUE] = True

    # Collect the integers from the Boolean array
    sorted_integers = [index + MIN_VALUE for index in range(RANGE_SIZE) if presence[index]]

    # Write sorted integers to the output file
    with open(output_file_path, 'w') as output_file:
        for number in sorted_integers:
            output_file.write(f"{number}\n")

    # Print message indicating completion
    print(f"Unique integers written to {output_file_path}")

# Example usage
process_file("results_for_sample_inputs/results_for_sample_inputs/sample_01.txt_result.txt", "sample_input_for_students/sample_input_for_students/sample_01.txt")
