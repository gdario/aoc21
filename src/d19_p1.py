def read_data(file_path: str) -> dict:
    lines = [line for line in open(file_path, "r").read().splitlines()
             if line != ""]
    data = dict()
    k = -1
    for line in lines:
        if line.startswith("---"):
            k += 1
            data[k] = []
        else:
            data[k].append([int(x) for x in line.split(",")])
    return data


if __name__ == "__main__":
    data = read_data("data/d19_p1_test.txt")
    print(data[2])