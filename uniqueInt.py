def process_file(input_file_path, output_file_path):
    
    MIN_VALUE, MAX_VALUE = -1023, 1023
    RANGE_SIZE = MAX_VALUE - MIN_VALUE + 1

    
    presence = [False] * RANGE_SIZE

    
    with open(input_file_path, 'r') as input_file:
        
        for line in input_file:
            stripped_line = line.strip()
            if stripped_line.startswith('-') and stripped_line[1:].isdigit() or stripped_line.isdigit():
                number = int(stripped_line)
                if MIN_VALUE <= number <= MAX_VALUE:
                    presence[number - MIN_VALUE] = True

    
    sorted_integers = [index + MIN_VALUE for index in range(RANGE_SIZE) if presence[index]]

    
    with open(output_file_path, 'w') as output_file:
        for number in sorted_integers:
            output_file.write(f"{number}\n")

    
    print(f"Unique integers written to {output_file_path}")


process_file("results_for_sample_inputs/results_for_sample_inputs/sample_01.txt_result.txt", "sample_input_for_students/sample_input_for_students/sample_01.txt")
