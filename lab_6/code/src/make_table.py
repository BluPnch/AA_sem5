import re

def process_line(line):
    pattern = r"Alpha: (\d+\.\d+), ro: (\d+\.\d+), Tmax: (\d+), Results: ([\d\.]+), ([\d\.]+), ([\d\.]+)"
    match = re.match(pattern, line)

    if match:
        # alpha = match.group(1)
        # ro = match.group(2)
        # tmax = match.group(3)
        result1 = match.group(4)
        result2 = match.group(5)
        result3 = match.group(6)
        # return f"{alpha} & {ro} & {tmax} & {result1} & {result2} & {result3}"
        return f" & {result1} & {result2} & {result3}"
    else:
        return None


def process_input(input_lines):
    output_lines = []

    for line in input_lines:
        processed_line = process_line(line)
        if processed_line:
            output_lines.append(processed_line)

    return output_lines


# def write_to_file(output_lines, filename):
#     with open(filename, 'w') as file:
#         for line in output_lines:
#             file.write(line + "\n")

def write_to_file(output_lines, filename):
    f = open("new_output_3.txt", "w")
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            new_line = lines[i][:-1] + output_lines[i]
            f.write(new_line + "\n")
            print(lines[i])
    f.close()


def write_to_file_hline(filename):
    f = open("new_new_output.txt", "w")
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            new_line = lines[i][:-1] + " \\ \hline"
            f.write(new_line + "\n")
            print(lines[i])
    f.close()
write_to_file_hline("new_output_3.txt")

def write_to_file_kavichki(filename):
    f = open("output.txt", "w")
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            new_line = '"' + lines[i][:-1] + '",'
            f.write(new_line + "\n")
            print(lines[i])
    f.close()
# write_to_file_kavichki("in")


input_strings = [
"Alpha: 0.1, ro: 0.1, Tmax: 20, Results: 299.245, 62.742, 96.144",
"Alpha: 0.1, ro: 0.1, Tmax: 50, Results: 399.882, 31.371, 91.886",
"Alpha: 0.1, ro: 0.1, Tmax: 100, Results: 5.513, 0.000, 1.103",
"Alpha: 0.1, ro: 0.1, Tmax: 150, Results: 5.513, 0.000, 0.551",
"Alpha: 0.1, ro: 0.1, Tmax: 200, Results: 2513.542, 0.000, 251.354",
"Alpha: 0.1, ro: 0.25, Tmax: 20, Results: 313.863, 31.371, 108.795",
"Alpha: 0.1, ro: 0.25, Tmax: 50, Results: 194.455, 2.756, 39.520",
"Alpha: 0.1, ro: 0.25, Tmax: 100, Results: 62.742, 2.756, 19.925",
"Alpha: 0.1, ro: 0.25, Tmax: 150, Results: 0.000, 0.000, 0.000",
"Alpha: 0.1, ro: 0.25, Tmax: 200, Results: 2162.053, 0.000, 216.205",
"Alpha: 0.1, ro: 0.5, Tmax: 20, Results: 319.644, 197.212, 152.900",
"Alpha: 0.1, ro: 0.5, Tmax: 50, Results: 193.241, 0.000, 32.573",
"Alpha: 0.1, ro: 0.5, Tmax: 100, Results: 3712.885, 0.000, 378.665",
"Alpha: 0.1, ro: 0.5, Tmax: 150, Results: 0.000, 0.000, 0.000",
"Alpha: 0.1, ro: 0.5, Tmax: 200, Results: 3023.481, 0.000, 302.348",
"Alpha: 0.1, ro: 0.75, Tmax: 20, Results: 193.241, 5.513, 41.202",
"Alpha: 0.1, ro: 0.75, Tmax: 50, Results: 2303.275, 0.000, 250.876",
"Alpha: 0.1, ro: 0.75, Tmax: 100, Results: 0.000, 0.000, 0.000",
"Alpha: 0.1, ro: 0.75, Tmax: 150, Results: 0.000, 0.000, 0.000",
"Alpha: 0.1, ro: 0.75, Tmax: 200, Results: 0.000, 0.000, 0.000",
"Alpha: 0.1, ro: 0.9, Tmax: 20, Results: 253.914, 62.742, 86.011",
"Alpha: 0.1, ro: 0.9, Tmax: 50, Results: 194.455, 5.513, 27.925",
"Alpha: 0.1, ro: 0.9, Tmax: 100, Results: 5.513, 0.000, 0.551",
"Alpha: 0.1, ro: 0.9, Tmax: 150, Results: 0.000, 0.000, 0.000",
"Alpha: 0.1, ro: 0.9, Tmax: 200, Results: 0.000, 0.000, 0.000",
"Alpha: 0.25, ro: 0.1, Tmax: 20, Results: 199.968, 34.127, 72.688",
"Alpha: 0.25, ro: 0.1, Tmax: 50, Results: 194.455, 0.000, 26.271",
"Alpha: 0.25, ro: 0.1, Tmax: 100, Results: 2052.874, 0.000, 218.537",
"Alpha: 0.25, ro: 0.1, Tmax: 150, Results: 5.513, 0.000, 0.551",
"Alpha: 0.25, ro: 0.1, Tmax: 200, Results: 0.000, 0.000, 0.000",
"Alpha: 0.25, ro: 0.25, Tmax: 20, Results: 262.979, 132.103, 124.929",
"Alpha: 0.25, ro: 0.25, Tmax: 50, Results: 193.241, 5.513, 33.526",
"Alpha: 0.25, ro: 0.25, Tmax: 100, Results: 0.000, 0.000, 0.000",
"Alpha: 0.25, ro: 0.25, Tmax: 150, Results: 0.000, 0.000, 0.000",
"Alpha: 0.25, ro: 0.25, Tmax: 200, Results: 3163.578, 0.000, 318.012",
"Alpha: 0.25, ro: 0.5, Tmax: 20, Results: 302.969, 194.455, 163.991",
"Alpha: 0.25, ro: 0.5, Tmax: 50, Results: 194.455, 34.127, 46.346",
"Alpha: 0.25, ro: 0.5, Tmax: 100, Results: 5.513, 0.000, 0.551",
"Alpha: 0.25, ro: 0.5, Tmax: 150, Results: 2879.747, 0.000, 287.975",
"Alpha: 0.25, ro: 0.5, Tmax: 200, Results: 2948.569, 0.000, 294.857",
"Alpha: 0.25, ro: 0.75, Tmax: 20, Results: 262.979, 2.756, 60.095",
"Alpha: 0.25, ro: 0.75, Tmax: 50, Results: 253.914, 0.000, 25.943",
"Alpha: 0.25, ro: 0.75, Tmax: 100, Results: 3204.131, 0.000, 326.687",
"Alpha: 0.25, ro: 0.75, Tmax: 150, Results: 5.513, 0.000, 0.551",
"Alpha: 0.25, ro: 0.75, Tmax: 200, Results: 0.000, 0.000, 0.000",
"Alpha: 0.25, ro: 0.9, Tmax: 20, Results: 302.969, 2.756, 57.699",
"Alpha: 0.25, ro: 0.9, Tmax: 50, Results: 69.750, 2.756, 20.626",
"Alpha: 0.25, ro: 0.9, Tmax: 100, Results: 62.742, 0.000, 6.274",
"Alpha: 0.25, ro: 0.9, Tmax: 150, Results: 0.000, 0.000, 0.000",
"Alpha: 0.25, ro: 0.9, Tmax: 200, Results: 0.000, 0.000, 0.000",
"Alpha: 0.5, ro: 0.1, Tmax: 20, Results: 313.863, 131.495, 123.305",
"Alpha: 0.5, ro: 0.1, Tmax: 50, Results: 262.979, 2.756, 45.672",
"Alpha: 0.5, ro: 0.1, Tmax: 100, Results: 69.750, 0.000, 8.078",
"Alpha: 0.5, ro: 0.1, Tmax: 150, Results: 62.742, 0.000, 13.100",
"Alpha: 0.5, ro: 0.1, Tmax: 200, Results: 0.000, 0.000, 0.000",
"Alpha: 0.5, ro: 0.25, Tmax: 20, Results: 324.494, 196.604, 183.002",
"Alpha: 0.5, ro: 0.25, Tmax: 50, Results: 69.750, 2.756, 20.626",
"Alpha: 0.5, ro: 0.25, Tmax: 100, Results: 62.742, 0.000, 7.377",
"Alpha: 0.5, ro: 0.25, Tmax: 150, Results: 0.000, 0.000, 0.000",
"Alpha: 0.5, ro: 0.25, Tmax: 200, Results: 0.000, 0.000, 0.000",
"Alpha: 0.5, ro: 0.5, Tmax: 20, Results: 324.494, 66.246, 137.346",
"Alpha: 0.5, ro: 0.5, Tmax: 50, Results: 194.455, 5.513, 52.972",
"Alpha: 0.5, ro: 0.5, Tmax: 100, Results: 3909.975, 0.000, 430.440",
"Alpha: 0.5, ro: 0.5, Tmax: 150, Results: 0.000, 0.000, 0.000",
"Alpha: 0.5, ro: 0.5, Tmax: 200, Results: 2362.289, 0.000, 371.220",
"Alpha: 0.5, ro: 0.75, Tmax: 20, Results: 305.026, 132.103, 134.883",
"Alpha: 0.5, ro: 0.75, Tmax: 50, Results: 194.455, 0.000, 32.545",
"Alpha: 0.5, ro: 0.75, Tmax: 100, Results: 62.742, 0.000, 7.377",
"Alpha: 0.5, ro: 0.75, Tmax: 150, Results: 5.513, 0.000, 0.551",
"Alpha: 0.5, ro: 0.75, Tmax: 200, Results: 0.000, 0.000, 0.000",
"Alpha: 0.5, ro: 0.9, Tmax: 20, Results: 269.987, 5.513, 92.384",
"Alpha: 0.5, ro: 0.9, Tmax: 50, Results: 194.455, 2.756, 33.097",
"Alpha: 0.5, ro: 0.9, Tmax: 100, Results: 5.513, 0.000, 0.551",
"Alpha: 0.5, ro: 0.9, Tmax: 150, Results: 0.000, 0.000, 0.000",
"Alpha: 0.5, ro: 0.9, Tmax: 200, Results: 0.000, 0.000, 0.000",
"Alpha: 0.75, ro: 0.1, Tmax: 20, Results: 808.615, 397.799, 422.804",
"Alpha: 0.75, ro: 0.1, Tmax: 50, Results: 319.644, 194.455, 154.246",
"Alpha: 0.75, ro: 0.1, Tmax: 100, Results: 194.455, 0.000, 26.822",
"Alpha: 0.75, ro: 0.1, Tmax: 150, Results: 62.742, 0.000, 6.825",
"Alpha: 0.75, ro: 0.1, Tmax: 200, Results: 62.742, 0.000, 6.274",
"Alpha: 0.75, ro: 0.25, Tmax: 20, Results: 822.641, 289.204, 326.780",
"Alpha: 0.75, ro: 0.25, Tmax: 50, Results: 262.979, 5.513, 92.785",
"Alpha: 0.75, ro: 0.25, Tmax: 100, Results: 62.742, 0.000, 7.377",
"Alpha: 0.75, ro: 0.25, Tmax: 150, Results: 62.742, 2.756, 19.925",
"Alpha: 0.75, ro: 0.25, Tmax: 200, Results: 194.455, 0.000, 19.446",
"Alpha: 0.75, ro: 0.5, Tmax: 20, Results: 684.726, 306.554, 310.701",
"Alpha: 0.75, ro: 0.5, Tmax: 50, Results: 62.742, 5.513, 9.031",
"Alpha: 0.75, ro: 0.5, Tmax: 100, Results: 5.513, 0.000, 1.103",
"Alpha: 0.75, ro: 0.5, Tmax: 150, Results: 0.000, 0.000, 0.000",
"Alpha: 0.75, ro: 0.5, Tmax: 200, Results: 0.000, 0.000, 0.000",
"Alpha: 0.75, ro: 0.75, Tmax: 20, Results: 262.979, 253.914, 194.745",
"Alpha: 0.75, ro: 0.75, Tmax: 50, Results: 199.968, 34.127, 45.645",
"Alpha: 0.75, ro: 0.75, Tmax: 100, Results: 5.513, 0.000, 1.654",
"Alpha: 0.75, ro: 0.75, Tmax: 150, Results: 5.513, 0.000, 1.103",
"Alpha: 0.75, ro: 0.75, Tmax: 200, Results: 4605.720, 0.000, 460.572",
"Alpha: 0.75, ro: 0.9, Tmax: 20, Results: 558.940, 132.103, 183.648",
"Alpha: 0.75, ro: 0.9, Tmax: 50, Results: 269.987, 5.513, 93.290",
"Alpha: 0.75, ro: 0.9, Tmax: 100, Results: 62.742, 0.000, 12.548",
"Alpha: 0.75, ro: 0.9, Tmax: 150, Results: 0.000, 0.000, 0.000",
"Alpha: 0.75, ro: 0.9, Tmax: 200, Results: 193.241, 0.000, 19.875",
"Alpha: 0.9, ro: 0.1, Tmax: 20, Results: 789.054, 410.944, 422.356",
"Alpha: 0.9, ro: 0.1, Tmax: 50, Results: 619.863, 196.604, 211.206",
"Alpha: 0.9, ro: 0.1, Tmax: 100, Results: 262.979, 0.000, 40.098",
"Alpha: 0.9, ro: 0.1, Tmax: 150, Results: 69.750, 0.000, 6.975",
"Alpha: 0.9, ro: 0.1, Tmax: 200, Results: 62.742, 0.000, 6.274",
"Alpha: 0.9, ro: 0.25, Tmax: 20, Results: 687.198, 312.688, 342.539",
"Alpha: 0.9, ro: 0.25, Tmax: 50, Results: 274.653, 197.212, 164.893",
"Alpha: 0.9, ro: 0.25, Tmax: 100, Results: 69.750, 0.000, 7.592",
"Alpha: 0.9, ro: 0.25, Tmax: 150, Results: 69.750, 0.000, 7.526",
"Alpha: 0.9, ro: 0.25, Tmax: 200, Results: 62.742, 0.000, 6.274",
"Alpha: 0.9, ro: 0.5, Tmax: 20, Results: 525.958, 346.460, 305.631",
"Alpha: 0.9, ro: 0.5, Tmax: 50, Results: 425.445, 66.246, 103.314",
"Alpha: 0.9, ro: 0.5, Tmax: 100, Results: 194.455, 2.756, 38.819",
"Alpha: 0.9, ro: 0.5, Tmax: 150, Results: 194.455, 0.000, 26.972",
"Alpha: 0.9, ro: 0.5, Tmax: 200, Results: 5.513, 0.000, 0.551",
"Alpha: 0.9, ro: 0.75, Tmax: 20, Results: 556.550, 262.979, 237.806",
"Alpha: 0.9, ro: 0.75, Tmax: 50, Results: 255.971, 5.513, 58.694",
"Alpha: 0.9, ro: 0.75, Tmax: 100, Results: 253.914, 0.000, 44.837",
"Alpha: 0.9, ro: 0.75, Tmax: 150, Results: 0.000, 0.000, 0.000",
"Alpha: 0.9, ro: 0.75, Tmax: 200, Results: 0.000, 0.000, 0.000",
"Alpha: 0.9, ro: 0.9, Tmax: 20, Results: 1072.390, 224.185, 271.123",
"Alpha: 0.9, ro: 0.9, Tmax: 50, Results: 274.653, 66.246, 105.905",
"Alpha: 0.9, ro: 0.9, Tmax: 100, Results: 259.695, 0.000, 27.623",
"Alpha: 0.9, ro: 0.9, Tmax: 150, Results: 69.750, 0.000, 6.975",
"Alpha: 0.9, ro: 0.9, Tmax: 200, Results: 5.513, 0.000, 0.55"
]


# output_data = process_input(input_strings)
# write_to_file(output_data, "new_output_2.txt")
