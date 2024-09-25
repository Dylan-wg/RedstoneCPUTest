import mcschematic
from mcschematic import MCSchematic

reflection = {
    "add": 0b00001,
    "sub": 0b00010,
    "nor": 0b00011,
    "and": 0b00100,
    "nxor": 0b00101,
    "rs": 0b00110,
    "ls": 0b00111,
    "load": 0b01000,
    "move": 0b01001,
    "load_imm": 0b01010,
    "input": 0b01011,
    "output": 0b01100,
    "jump": 0b01101,
    "jnep": 0b01110,
    "jneg": 0b01111,
    "jodd": 0b10000,
    "halt": 0b10001
}

pos = [
    [1, 0, 0],
    [1, -3, -1],
    [1, -4, 0],
    [1, -7, -1],
    [1, -8, 0],
    [1, -11, -1],
    [1, -12, 0],
    [1, -15, -1],

    [1, -1, -2],
    [1, -2, -3],
    [1, -5, -2],
    [1, -6, -3],
    [1, -9, -2],
    [1, -10, -3],
    [1, -13, -2],
    [1, -14, -3]
]


def int_to_binary_list(n):
    binary_str = bin(n)[2:].zfill(8)
    return [int(bit) for bit in binary_str]


def generate_nbt(machine_code: list, file):
    schem = MCSchematic()
    chart = []
    for j in machine_code:
        chart += int_to_binary_list(j)
    for i in range(0, 4):
        for p in pos:
            index = pos.index(p) + 16 * i
            try:
                if chart[index] == 1:
                    schem.setBlock((p[0], p[1], p[2] + i * (-4)), "minecraft:redstone_wall_torch[facing=west]")
                elif chart[index] == 0:
                    schem.setBlock((p[0], p[1], p[2] + i * (-4)), "minecraft:air")
            except IndexError:
                pass

    schem.save("./", file, mcschematic.Version.JE_1_19)


def main(file_name):
    start_0 = input("Start with zero?")
    machine_code: list = [0]
    if start_0 == "y":
        machine_code = []
    elif start_0 == "n":
        machine_code = [0]
    double_bit: bool = False
    try:
        with open("./" + file_name + ".txt", "r", encoding="utf-8") as file:
            code = file.read()
            code = code.split("\n")
    except FileNotFoundError:
        return

    for line in code:
        depart = line.split(" ")
        new_line = 0b0
        if not double_bit:
            new_line += reflection[depart[0]]
            if len(depart) == 1:
                new_line = new_line << 3
            else:
                new_line = (new_line << 3) + int(depart[1])
            machine_code.append(new_line)
            if depart[0] in ["load_imm", "jump", "jnep", "jneg", "jodd"]:
                double_bit = True
        elif double_bit:
            new_line = int(depart[0])
            machine_code.append(new_line)
            double_bit = False

    generate_nbt(machine_code, file_name)
    print("Machine code:" + str(machine_code))
    print("Done.")


if __name__ == "__main__":
    file = input("File name:")
    main(file)
