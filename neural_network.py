MIN_INPUT_1 = 0
MAX_INPUT_1 = 800
MIN_INPUT_2 = 0
MAX_INPUT_2 = 600

def normalize_input(input_value, min_input, max_input):
    # Scale input_value to the range [0, 1]
    return (input_value - min_input) / (max_input - min_input)

def Classify(input_1, input_2, weight_1_1, weight_2_1, weight_1_2, weight_2_2, bias_1, bias_2):
    # Normalize inputs
    input_1_normalized = normalize_input(input_1, MIN_INPUT_1, MAX_INPUT_1)
    input_2_normalized = normalize_input(input_2, MIN_INPUT_2, MAX_INPUT_2)

    # Calculate outputs
    output_1 = (input_1_normalized * weight_1_1) + (input_2_normalized * weight_2_1) + bias_1
    output_2 = (input_1_normalized * weight_1_2) + (input_2_normalized * weight_2_2) + bias_2

    # Ensure output values fall within the range of -1 to 0
    # output_1 = max(min(output_1, 0), -1)
    # output_2 = max(min(output_2, 0), -1)

    # Classify based on outputs
    return 0 if output_1 > output_2 else 1
