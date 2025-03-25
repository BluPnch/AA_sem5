# Укажите имя исходного и выходного файла
input_file = 'C:\\Users\\varya\\AA\\lab_6\\code\\src\\in'
output_file = 'C:\\Users\\varya\\AA\\lab_6\\code\\src\\output.txt'

def write_to_file():
    with open(output_file, "w") as f:
        with open(input_file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                elems = line.strip().split(' & ')
                print(elems)
                f.write(f"{elems[0]} & {elems[1]} & {elems[2]} & ")
                for i in range(3, len(elems) - 1):
                    f.write(f"{int(float(elems[i]))} & ")
                last_value = int(float(elems[-1].replace('\\\\ \\hline', '').strip()))
                f.write(f"{last_value} \\\ \hline\n")

write_to_file()
