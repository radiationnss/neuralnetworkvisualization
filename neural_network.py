def Classify(input_1, input_2, weight_1_1, weight_2_1, weight_1_2, weight_2_2):
    output_1 = (input_1 * weight_1_1) + (input_2 * weight_2_1)
    output_2 = (input_1 * weight_1_2) + (input_2 * weight_2_2)

    return 0 if output_1 > output_2 else 1
